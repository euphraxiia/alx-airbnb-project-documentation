# User Stories - Airbnb Clone Backend

This document contains user stories derived from the use case diagram. Each user story follows the format:

**As a [user type], I want to [action], so that [benefit/value].**

---

## Guest User Stories

### Authentication & Profile

**US-G001: User Registration**
- **As a** guest,
- **I want to** register an account with email and password,
- **So that** I can access the platform and start booking properties.

**US-G002: User Login**
- **As a** guest,
- **I want to** login to my account using email and password or OAuth providers,
- **So that** I can access my bookings and manage my profile.

**US-G003: Email Verification**
- **As a** guest,
- **I want to** verify my email address after registration,
- **So that** I can ensure my account is secure and receive important notifications.

**US-G004: Profile Management**
- **As a** guest,
- **I want to** manage my profile information (name, bio, profile picture),
- **So that** hosts can learn about me when I request bookings.

---

### Search & Discovery

**US-G005: Search Listings**
- **As a** guest,
- **I want to** search for properties by location, dates, and guest count,
- **So that** I can find available accommodations that meet my needs.

**US-G006: View Listing Details**
- **As a** guest,
- **I want to** view detailed information about a property including photos, amenities, and reviews,
- **So that** I can make an informed decision about booking.

---

### Booking Management

**US-G007: Book Property**
- **As a** guest,
- **I want to** book a property for specific dates,
- **So that** I can reserve my accommodation in advance.

**US-G008: Manage Booking**
- **As a** guest,
- **I want to** view and manage my bookings (upcoming, past, cancelled),
- **So that** I can track my travel plans and booking history.

**US-G009: Cancel Booking**
- **As a** guest,
- **I want to** cancel a booking according to the cancellation policy,
- **So that** I can receive a refund when my plans change.

---

### Payment

**US-G010: Make Payment**
- **As a** guest,
- **I want to** securely pay for my booking using credit cards or digital wallets,
- **So that** I can complete my reservation and confirm my booking.

**US-G011: Request Refund**
- **As a** guest,
- **I want to** receive refunds when I cancel eligible bookings,
- **So that** I can recover my money according to the cancellation policy.

---

### Communication & Reviews

**US-G012: Message Host**
- **As a** guest,
- **I want to** send messages to hosts before and during my stay,
- **So that** I can ask questions, get check-in instructions, and communicate about my stay.

**US-G013: Leave Review**
- **As a** guest,
- **I want to** leave a review and rating after my stay,
- **So that** I can help other guests make informed decisions and provide feedback to hosts.

---

### Notifications

**US-G014: Receive Notifications**
- **As a** guest,
- **I want to** receive notifications about booking confirmations, messages, and reminders,
- **So that** I stay informed about important updates regarding my bookings.

---

## Host User Stories

### Property Management

**US-H001: List Property**
- **As a** host,
- **I want to** create a new property listing with details, photos, and pricing,
- **So that** I can make my property available for guests to book.

**US-H002: Manage Listing**
- **As a** host,
- **I want to** update my property listing information (description, amenities, pricing),
- **So that** I can keep my listing accurate and attractive to guests.

**US-H003: Set Availability**
- **As a** host,
- **I want to** set and manage my property's availability calendar,
- **So that** I can control when my property is available for booking.

---

### Booking Management

**US-H004: Manage Booking Requests**
- **As a** host,
- **I want to** accept or decline booking requests from guests,
- **So that** I can control who stays at my property.

**US-H005: View Booking Details**
- **As a** host,
- **I want to** view details of all bookings for my properties,
- **So that** I can prepare for guest arrivals and manage my rental business.

---

### Communication & Reviews

**US-H006: Message Guest**
- **As a** host,
- **I want to** send messages to guests,
- **So that** I can provide check-in instructions, answer questions, and communicate during their stay.

**US-H007: Review Guest**
- **As a** host,
- **I want to** leave a review about guests after their stay,
- **So that** I can provide feedback to help other hosts make informed decisions.

---

### Payment

**US-H008: Receive Payouts**
- **As a** host,
- **I want to** receive payouts from bookings after guest checkout,
- **So that** I can receive payment for providing accommodation services.

---

### Notifications

**US-H009: Receive Booking Notifications**
- **As a** host,
- **I want to** receive notifications about new booking requests, messages, and reviews,
- **So that** I can respond promptly to guests and manage my listings effectively.

---

## Admin User Stories

### User Management

**US-A001: Moderate Users**
- **As an** administrator,
- **I want to** view, verify, suspend, or delete user accounts,
- **So that** I can maintain platform security and ensure user authenticity.

---

### Property Management

**US-A002: Moderate Properties**
- **As an** administrator,
- **I want to** review, approve, reject, or flag property listings,
- **So that** I can ensure all listings meet platform quality and safety standards.

---

### Booking Management

**US-A003: Moderate Bookings**
- **As an** administrator,
- **I want to** view and intervene in bookings when disputes arise,
- **So that** I can resolve conflicts and ensure fair resolution between guests and hosts.

---

### Notifications

**US-A004: Receive System Notifications**
- **As an** administrator,
- **I want to** receive notifications about platform issues, disputes, and critical events,
- **So that** I can respond quickly to maintain platform quality and user satisfaction.

---

## Priority User Stories (Core Interactions)

These are the 5 most critical user stories that capture the core interactions from the use case diagram:

1. **US-G001: User Registration** - As a guest, I want to register an account with email and password, so that I can access the platform and start booking properties.

2. **US-G007: Book Property** - As a guest, I want to book a property for specific dates, so that I can reserve my accommodation in advance.

3. **US-G010: Make Payment** - As a guest, I want to securely pay for my booking using credit cards or digital wallets, so that I can complete my reservation and confirm my booking.

4. **US-H001: List Property** - As a host, I want to create a new property listing with details, photos, and pricing, so that I can make my property available for guests to book.

5. **US-G013: Leave Review** - As a guest, I want to leave a review and rating after my stay, so that I can help other guests make informed decisions and provide feedback to hosts.

---

## User Story Mapping

### By Actor
- **Guest**: 14 user stories (US-G001 to US-G014)
- **Host**: 9 user stories (US-H001 to US-H009)
- **Admin**: 4 user stories (US-A001 to US-A004)

### By Feature Area
- **Authentication & Profile**: 4 stories
- **Search & Discovery**: 2 stories
- **Booking Management**: 5 stories
- **Payment**: 3 stories
- **Property Management**: 3 stories
- **Communication & Reviews**: 4 stories
- **Administration**: 3 stories
- **Notifications**: 3 stories

---

**Total User Stories**: 27
**Priority Stories**: 5 (core interactions)
**Last Updated**: October 29, 2024

