import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch

fig, ax = plt.subplots(figsize=(20, 14))
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.axis('off')

# Helper to draw actor as a labeled rounded box
def draw_actor(x, y, label):
    box = FancyBboxPatch((x-1.4, y-0.6), 2.8, 1.2, boxstyle="round,pad=0.2",
                         facecolor="#f7f7f7", edgecolor="#333", linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=11, fontweight='bold')

# Helper to draw use case (ellipse)
def draw_usecase(x, y, label, w=3.8, h=1.6):
    e = Ellipse((x, y), width=w, height=h, facecolor="#e8f1ff", edgecolor="#2c5aa0", linewidth=1.8)
    ax.add_patch(e)
    ax.text(x, y, label, ha='center', va='center', fontsize=10)

# Helper to connect actor to use case
def connect(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color="#666", linewidth=1.4)

# Actors
actors = {
    'Guest': (2, 12),
    'Host': (2, 8.5),
    'Admin': (2, 5.0),
    'Payment Provider': (18, 9.5),
    'Email Service': (18, 6.0),
}
for name, (x, y) in actors.items():
    draw_actor(x, y, name)

# Use case clusters (group visually by modules)
# Authentication
draw_usecase(7.5, 12.0, 'Register Account')
draw_usecase(7.5, 10.0, 'Login')
draw_usecase(7.5, 8.0, 'Verify Email')
# Profile
draw_usecase(7.5, 6.0, 'Manage Profile')
# Search & View
draw_usecase(10.5, 12.0, 'Search Listings')
draw_usecase(10.5, 10.0, 'View Listing Details')
# Booking
draw_usecase(10.5, 8.0, 'Book Property')
draw_usecase(10.5, 6.0, 'Manage Booking')
draw_usecase(10.5, 4.2, 'Cancel Booking')
# Payment
draw_usecase(13.5, 8.0, 'Make Payment')
draw_usecase(13.5, 6.0, 'Refund Payment')
# Host listing
draw_usecase(7.5, 4.2, 'List Property')
draw_usecase(7.5, 2.6, 'Manage Listing')
draw_usecase(10.5, 2.6, 'Set Availability')
# Messaging & Reviews
draw_usecase(13.5, 12.0, 'Message Host/Guest')
draw_usecase(13.5, 10.0, 'Leave Review')
# Admin
draw_usecase(7.5, 0.9, 'Moderate Users')
draw_usecase(10.5, 0.9, 'Moderate Properties')
draw_usecase(13.5, 0.9, 'Moderate Bookings')
# Notifications
draw_usecase(16.5, 4.2, 'Receive Notifications')

# Connections from Guest
gx, gy = actors['Guest']
for (ux, uy) in [(7.5,12.0),(7.5,10.0),(7.5,8.0),(7.5,6.0),(10.5,12.0),(10.5,10.0),(10.5,8.0),(10.5,6.0),(10.5,4.2),(13.5,12.0),(13.5,10.0),(13.5,8.0),(13.5,6.0),(16.5,4.2)]:
    connect(gx+1.4, gy, ux-2.0, uy)

# Connections from Host
hx, hy = actors['Host']
for (ux, uy) in [(7.5,6.0),(7.5,4.2),(7.5,2.6),(10.5,2.6),(10.5,6.0),(13.5,12.0),(16.5,4.2)]:
    connect(hx+1.4, hy, ux-2.0, uy)

# Connections from Admin
ax_x, ax_y = actors['Admin']
for (ux, uy) in [(7.5,0.9),(10.5,0.9),(13.5,0.9),(16.5,4.2)]:
    connect(ax_x+1.4, ax_y, ux-2.0, uy)

# External systems
px, py = actors['Payment Provider']
for (ux, uy) in [(13.5,8.0),(13.5,6.0)]:
    connect(px-1.4, py, ux+2.0, uy)

ex, ey = actors['Email Service']
for (ux, uy) in [(7.5,8.0)]:  # Verify Email
    connect(ex-1.4, ey, ux+2.0, uy)

# Title
ax.text(10, 13.6, 'Airbnb Clone - Use Case Diagram', ha='center', va='center', fontsize=18, fontweight='bold')

plt.tight_layout()
fig.savefig('/Users/boitumelomahlaha/Desktop/alx-airbnb-project-documentation/use-case-diagram/use_case_diagram.png', dpi=300, bbox_inches='tight')
print('Generated use_case_diagram.png')
