#!/usr/bin/env python3
"""
Generate a comprehensive feature diagram for Airbnb Clone Backend
Exports as PNG file without requiring Draw.io
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, ConnectionPatch
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(20, 16))
ax.set_xlim(0, 20)
ax.set_ylim(0, 16)
ax.axis('off')

# Define colors
colors = {
    'auth': '#4A90E2',
    'property': '#50C878',
    'booking': '#FF6B6B',
    'payment': '#FFD93D',
    'review': '#9B59B6',
    'search': '#3498DB',
    'message': '#E67E22',
    'image': '#1ABC9C',
    'notification': '#34495E',
    'admin': '#E74C3C',
    'additional': '#95A5A6'
}

# Define feature boxes with positions and sizes
features = [
    # Row 1 - Core Features
    {'name': 'User Authentication\n&\nAuthorization', 'pos': (1, 13), 'size': (3.5, 2.5), 'color': colors['auth'],
     'details': ['Registration', 'Login', 'OAuth', 'Profile', 'Roles']},
    
    {'name': 'Property\nManagement', 'pos': (5.5, 13), 'size': (3.5, 2.5), 'color': colors['property'],
     'details': ['CRUD', 'Location', 'Pricing', 'Amenities', 'Calendar']},
    
    {'name': 'Booking\nSystem', 'pos': (10, 13), 'size': (3.5, 2.5), 'color': colors['booking'],
     'details': ['Create', 'Manage', 'Status', 'Cancellation']},
    
    {'name': 'Payment\nProcessing', 'pos': (14.5, 13), 'size': (3.5, 2.5), 'color': colors['payment'],
     'details': ['Gateway', 'Transactions', 'Payouts', 'Refunds']},
    
    # Row 2 - Secondary Features
    {'name': 'Reviews &\nRatings', 'pos': (1, 9.5), 'size': (3.5, 2.5), 'color': colors['review'],
     'details': ['Submit', 'Display', 'Moderate', 'Aggregate']},
    
    {'name': 'Search &\nFiltering', 'pos': (5.5, 9.5), 'size': (3.5, 2.5), 'color': colors['search'],
     'details': ['Location', 'Filters', 'Sorting', 'Map']},
    
    {'name': 'Messaging &\nCommunication', 'pos': (10, 9.5), 'size': (3.5, 2.5), 'color': colors['message'],
     'details': ['In-App', 'Threads', 'Notifications']},
    
    {'name': 'Image\nManagement', 'pos': (14.5, 9.5), 'size': (3.5, 2.5), 'color': colors['image'],
     'details': ['Upload', 'Storage', 'Optimization', 'CDN']},
    
    # Row 3 - Support Features
    {'name': 'Notifications\nSystem', 'pos': (1, 6), 'size': (3.5, 2.5), 'color': colors['notification'],
     'details': ['Email', 'Push', 'SMS', 'Preferences']},
    
    {'name': 'Admin\nDashboard', 'pos': (5.5, 6), 'size': (3.5, 2.5), 'color': colors['admin'],
     'details': ['Users', 'Properties', 'Bookings', 'Analytics']},
    
    {'name': 'Additional\nFeatures', 'pos': (10, 6), 'size': (3.5, 2.5), 'color': colors['additional'],
     'details': ['Wishlists', 'Recommendations', 'API', 'Analytics']},
    
    # Security - Bottom
    {'name': 'Security\nFeatures', 'pos': (14.5, 6), 'size': (3.5, 2.5), 'color': '#C0392B',
     'details': ['Encryption', 'HTTPS', 'Auth', 'Validation']},
]

# Draw feature boxes
for feature in features:
    x, y = feature['pos']
    w, h = feature['size']
    
    # Draw main box
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.1",
                         facecolor=feature['color'],
                         edgecolor='black',
                         linewidth=2,
                         alpha=0.8)
    ax.add_patch(box)
    
    # Add title
    ax.text(x + w/2, y + h - 0.4, feature['name'],
            ha='center', va='top', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))
    
    # Add details
    details_text = '\n'.join([f'• {d}' for d in feature['details']])
    ax.text(x + w/2, y + h/2 - 0.3, details_text,
            ha='center', va='center', fontsize=8)

# Title
ax.text(10, 15.5, 'Airbnb Clone Backend - Features & Functionalities',
        ha='center', va='top', fontsize=18, fontweight='bold')

# Draw connections/relationships
connections = [
    # Auth connects to everything
    (2.75, 13, 5.5, 11.25),   # Auth -> Property
    (5.25, 13, 10, 11.25),    # Auth -> Booking
    (9, 13, 14.5, 11.25),     # Booking -> Payment
    
    # Property connects to Booking
    (7.25, 13, 10, 13),       # Property -> Booking
    
    # Booking connects to Reviews
    (10, 12, 2.75, 11),       # Booking -> Reviews
    
    # Search connects to Property
    (7.25, 9.5, 5.5, 9.5),    # Search -> Property
    
    # Message connects to Booking
    (10, 9.5, 10, 11.25),     # Message <-> Booking
    
    # Image connects to Property
    (16.25, 9.5, 9, 13),      # Image -> Property
    
    # Admin connects to everything
    (7.25, 6, 3.25, 13),      # Admin -> Auth
    (7.25, 6, 7.25, 13),      # Admin -> Property
    (7.25, 6, 11.75, 13),     # Admin -> Booking
    (7.25, 6, 16.25, 13),     # Admin -> Payment
    
    # Notification connects to key features
    (2.75, 8, 10, 13),        # Notification -> Booking
    (2.75, 8, 11.75, 9.5),    # Notification -> Message
]

# Draw arrows for relationships
for conn in connections:
    arrow = FancyArrowPatch((conn[0], conn[1]), (conn[2], conn[3]),
                           arrowstyle='->', mutation_scale=20,
                           color='gray', linewidth=1.5, alpha=0.6,
                           connectionstyle="arc3,rad=0.1")
    ax.add_patch(arrow)

# Add legend
legend_elements = [
    mpatches.Patch(facecolor=colors['auth'], label='Authentication'),
    mpatches.Patch(facecolor=colors['property'], label='Property'),
    mpatches.Patch(facecolor=colors['booking'], label='Booking'),
    mpatches.Patch(facecolor=colors['payment'], label='Payment'),
    mpatches.Patch(facecolor=colors['review'], label='Reviews'),
    mpatches.Patch(facecolor=colors['search'], label='Search'),
    mpatches.Patch(facecolor=colors['message'], label='Messaging'),
    mpatches.Patch(facecolor=colors['image'], label='Images'),
    mpatches.Patch(facecolor=colors['notification'], label='Notifications'),
    mpatches.Patch(facecolor=colors['admin'], label='Admin'),
    mpatches.Patch(facecolor=colors['additional'], label='Additional'),
]

ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 0.02),
         ncol=6, fontsize=9, framealpha=0.9)

# Add technology stack box at the bottom
tech_box = FancyBboxPatch((1, 0.5), 18, 3,
                         boxstyle="round,pad=0.2",
                         facecolor='#ECF0F1',
                         edgecolor='black',
                         linewidth=2,
                         alpha=0.9)
ax.add_patch(tech_box)

ax.text(10, 3, 'Technology Stack',
        ha='center', va='top', fontsize=12, fontweight='bold')

tech_text = """Backend: Python (Flask/Django) | Node.js (Express) | Ruby on Rails
Database: PostgreSQL | MySQL | MongoDB | Caching: Redis
Storage: AWS S3 | Google Cloud | Payment: Stripe | PayPal
Email: SendGrid | Mailgun | Real-time: WebSockets | Search: Elasticsearch"""

ax.text(10, 2.2, tech_text,
        ha='center', va='top', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))

# Footer
ax.text(10, 0.1, 'Airbnb Clone Backend Architecture - Feature Overview',
        ha='center', va='bottom', fontsize=10, style='italic', color='gray')

plt.tight_layout()
plt.savefig('features-and-functionalities/backend_features_diagram.png',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("Diagram generated successfully: backend_features_diagram.png")
plt.close()

