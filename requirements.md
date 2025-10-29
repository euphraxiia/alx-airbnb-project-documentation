## Backend Requirements Specification

This document specifies functional and technical requirements for three core backend feature areas: User Authentication, Property Management, and Booking System.

### Conventions
- Authentication: Bearer JWT unless otherwise noted
- Content-Type: application/json
- Dates: ISO 8601 (UTC)
- IDs: UUID v4
- Pagination: cursor or page/limit; default limit 20; max 100

---

## 1) User Authentication

### Goals
- Secure account creation, login, session/token lifecycle, and password recovery.
- Support OAuth providers (extensible).

### API Endpoints

1. POST /api/v1/auth/register
- Auth: Public
- Request body:
```json
{
  "email": "user@example.com",
  "password": "Str0ngP@ss!",
  "firstName": "Ada",
  "lastName": "Lovelace"
}
```
- Validation:
  - email: valid RFC 5322, lowercased, unique
  - password: min 8 chars, at least 1 upper, 1 lower, 1 digit, 1 symbol
  - names: 1..80 chars, letters, spaces, hyphens
- Responses:
  - 201: { "userId": "uuid", "email": "...", "requiresEmailVerification": true }
  - 400: validation errors
  - 409: email already exists
- Side effects: send verification email (async job)

2. POST /api/v1/auth/login
- Auth: Public
- Request body:
```json
{ "email": "user@example.com", "password": "Str0ngP@ss!" }
```
- Responses:
  - 200: { "accessToken": "jwt", "refreshToken": "jwt", "user": { "id": "uuid", "email": "..." } }
  - 401: invalid credentials or unverified email (if policy enforces)
- Notes: account lockout after N failed attempts (e.g., 5 within 15 min)

3. POST /api/v1/auth/refresh
- Auth: Public (with refresh token)
- Request body: { "refreshToken": "jwt" }
- Responses:
  - 200: { "accessToken": "jwt", "refreshToken": "jwt" }
  - 401: invalid/expired token

4. POST /api/v1/auth/logout
- Auth: Bearer
- Invalidate refresh token (server-side blacklist/rotation)
- 204 No Content

5. POST /api/v1/auth/verify-email
- Auth: Public
- Request body: { "token": "signed-email-token" }
- 200 on success; 400/410 invalid/expired token

6. POST /api/v1/auth/forgot-password
- Auth: Public
- Request body: { "email": "user@example.com" }
- 202 Accepted (always) – do not reveal account existence
- Side effect: send reset email with signed, expiring token

7. POST /api/v1/auth/reset-password
- Auth: Public
- Request body: { "token": "reset-token", "newPassword": "Str0ngP@ss!" }
- 200 on success; 400/410 invalid/expired token

### Data Models (minimal)
- User: { id, email, passwordHash, firstName, lastName, emailVerifiedAt, createdAt, updatedAt, lastLoginAt, failedLoginCount, lockedUntil }
- RefreshToken: { id, userId, tokenHash, expiresAt, revokedAt, createdAt }

### Security & Validation
- Hash passwords with Argon2id or bcrypt(cost ≥ 12)
- JWT: RS256 signed, 15-min access, 30-day refresh (rotating)
- Enforce HTTPS, HSTS, SameSite=strict cookies if using cookies
- Brute-force protection: rate limiting and lockouts
- Audit log: login, logout, password reset, email verify

### Performance
- p50 < 100ms; p95 < 300ms for login/register (excluding email sending)
- Email jobs queued; queue processing within < 1 min

---

## 2) Property Management

### Goals
- CRUD for listings, media, availability, and pricing with host authorization.

### API Endpoints

1. POST /api/v1/properties
- Auth: Bearer (role: Host)
- Request body:
```json
{
  "title": "Modern Loft",
  "description": "Spacious loft...",
  "type": "apartment",
  "address": { "line1": "123 Main St", "city": "Berlin", "country": "DE", "postalCode": "10115" },
  "coordinates": { "lat": 52.5200, "lng": 13.4050 },
  "capacity": { "guests": 4, "bedrooms": 2, "beds": 2, "bathrooms": 1 },
  "amenities": ["wifi","kitchen","heating"],
  "pricing": { "baseNightly": 120.0, "currency": "EUR", "cleaningFee": 30.0, "extraGuestFee": 10.0 },
  "rules": { "smoking": false, "pets": true },
  "cancellationPolicy": "flexible"
}
```
- Validation:
  - title: 1..120; description: 1..4000; type: enum
  - coordinates: -90..90 lat, -180..180 lng
  - pricing.baseNightly ≥ 0; currency: ISO 4217
- Responses:
  - 201: { "id": "uuid", ... }
  - 400: validation errors

2. GET /api/v1/properties/{id}
- Auth: Public
- Response: property details with current availability summary
- 404 if not found or soft-deleted

3. PATCH /api/v1/properties/{id}
- Auth: Bearer (owner only or Admin)
- Request body: partial updates for fields above
- Response: 200 updated resource
- 403 if not owner

4. DELETE /api/v1/properties/{id}
- Auth: Bearer (owner/Admin)
- Soft-delete; disallow if active future bookings exist
- 204 No Content; 409 if constraint violated

5. POST /api/v1/properties/{id}/images
- Auth: Bearer (owner)
- Multipart/form-data: images[] (JPEG/PNG/WebP ≤ 10MB each)
- Response: 201 with array of stored image metadata { id, url, isCover }
- Validation: max 20 images per property

6. PUT /api/v1/properties/{id}/availability
- Auth: Bearer (owner)
- Request body:
```json
{
  "rules": { "minNights": 2, "maxNights": 28, "advanceNoticeDays": 1 },
  "blockedDates": ["2025-12-24","2025-12-25"],
  "seasonalPricing": [ { "start": "2025-06-01", "end": "2025-08-31", "nightly": 150.0 } ]
}
```
- Validation: non-overlapping date ranges; dates ≥ today
- Response: 200 updated configuration

7. GET /api/v1/properties/search
- Auth: Public
- Query params: q, city, lat,lng, radiusKm, startDate, endDate, guests, priceMin, priceMax, amenities[], sort, page, limit
- Response: 200 { items: [...], page, limit, total }
- Performance: must use indexes and availability precomputation for date range queries

### Data Models (minimal)
- Property: { id, ownerId, title, description, type, address, coordinates, capacity, amenities[], pricing, rules, cancellationPolicy, status, createdAt, updatedAt, deletedAt }
- PropertyImage: { id, propertyId, url, isCover, width, height, createdAt }
- AvailabilityRule: { propertyId, minNights, maxNights, advanceNoticeDays }
- BlockedDate: { propertyId, date }
- SeasonalPrice: { propertyId, start, end, nightly }

### Security & Validation
- Ownership checks on write operations
- Image scanning (virus/malware), MIME validation; store in S3/GCS with signed URLs
- Input sanitization to prevent HTML/script injection in descriptions

### Performance
- p95 search < 500ms for indexed queries (≤ 50 km radius)
- Use caching (Redis) for popular searches and property details
- Image uploads streamed; processing async (thumbnails)

---

## 3) Booking System

### Goals
- Reliable reservation lifecycle: quote → reserve → pay → confirm → complete/cancel/refund.

### API Endpoints

1. POST /api/v1/bookings/quote
- Auth: Public
- Request body:
```json
{
  "propertyId": "uuid",
  "startDate": "2025-07-10",
  "endDate": "2025-07-14",
  "guests": 2,
  "promoCode": "SUMMER25"
}
```
- Validation:
  - dates: start < end; duration within min/max nights; not blocked; not overlapping existing confirmed bookings
  - guests ≤ property.capacity.guests
- Response 200 example:
```json
{
  "currency": "EUR",
  "nights": 4,
  "breakdown": {
    "base": 480.0,
    "cleaningFee": 30.0,
    "discount": 25.0,
    "serviceFee": 40.0,
    "tax": 75.0
  },
  "total": 600.0
}
```

2. POST /api/v1/bookings
- Auth: Bearer (Guest)
- Request body:
```json
{
  "propertyId": "uuid",
  "startDate": "2025-07-10",
  "endDate": "2025-07-14",
  "guests": 2,
  "paymentMethodId": "pm_12345",
  "instantBook": true
}
```
- Flow:
  - Re-validate quote; place hold on availability (transaction/optimistic lock)
  - If instantBook=true, immediately attempt payment; else set status=pending_host
- Responses:
  - 201: { "id": "uuid", "status": "confirmed|pending_host|payment_failed", "total": 600.0 }
  - 409: availability conflict

3. GET /api/v1/bookings/{id}
- Auth: Bearer (owner of booking or property host or Admin)
- Response: booking details including status timeline, check-in/out, guests, total, payments[]

4. PATCH /api/v1/bookings/{id}/cancel
- Auth: Bearer (Guest or Host, according to policy)
- Request body: { "reason": "string" }
- Rules: compute refund per cancellationPolicy and time-to-checkin
- Response: 200 { "status": "cancelled", "refund": { "amount": 300.0, "currency": "EUR" } }

5. POST /api/v1/bookings/{id}/pay
- Auth: Bearer (Guest)
- Request body: { "paymentMethodId": "pm_12345" }
- Response: 200 { "paymentId": "uuid", "status": "succeeded|requires_action|failed" }
- Side effects: on succeeded → set booking confirmed; enqueue notifications

### Data Models (minimal)
- Booking: { id, propertyId, guestId, hostId, startDate, endDate, guests, currency, total, status, createdAt, updatedAt }
- Payment: { id, bookingId, amount, currency, provider, providerRef, status, createdAt }
- BookingEvent: { id, bookingId, type, at, meta }

### Concurrency & Integrity
- Prevent double-booking with serializable transaction or row-level locking on availability
- Idempotency keys on booking creation and payments
- Strong consistency for availability, eventual consistency for notifications/emails

### Notifications
- On creation, confirmation, cancellation, refund: email + in-app to guest and host

### Performance
- p95 booking creation < 700ms excluding external payment latency
- Precompute availability calendars; index by propertyId and date

---

## Non-Functional Requirements (Cross-cutting)

- Observability: structured logs, request IDs, tracing (OpenTelemetry), metrics (p95 latency, error rate)
- Rate limiting: per-IP and per-user on auth and booking endpoints
- API versioning: /api/v1; breaking changes require new version
- Documentation: OpenAPI 3.1 spec; generated SDKs when possible
- Backups: daily database backups with 14-day retention; tested restores

## Acceptance Criteria
- All listed endpoints return specified status codes and payloads
- Validation errors are precise with field-level messages
- Security controls (authN/Z, rate limiting) enforced per endpoint
- Performance targets met under expected load (baseline: 50 RPS aggregate)
