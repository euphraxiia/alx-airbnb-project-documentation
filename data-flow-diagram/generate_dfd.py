#!/usr/bin/env python3
"""
Generate a Data Flow Diagram (DFD) for Airbnb Clone Backend
Shows how data moves through the system
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.patches as mpatches

fig, ax = plt.subplots(1, 1, figsize=(22, 16))
ax.set_xlim(0, 22)
ax.set_ylim(0, 16)
ax.axis('off')

# Define colors
color_external = '#FFE5B4'  # Peach for external entities
color_process = '#E8F4F8'  # Light blue for processes
color_store = '#F0E68C'    # Khaki for data stores
color_flow = '#333333'     # Dark gray for flows

# Helper to draw external entity (rectangle)
def draw_external(x, y, label, w=2.5, h=1.2):
    box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                        boxstyle="round,pad=0.15",
                        facecolor=color_external,
                        edgecolor='black',
                        linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', 
           fontsize=10, fontweight='bold')

# Helper to draw process (rounded rectangle)
def draw_process(x, y, label, w=2.8, h=1.5):
    box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                        boxstyle="round,pad=0.2",
                        facecolor=color_process,
                        edgecolor='#2c5aa0',
                        linewidth=2)
    ax.add_patch(box)
    # Split label into lines if needed
    lines = label.split('\n')
    for i, line in enumerate(lines):
        ax.text(x, y + (len(lines)-1-i-0.5*(len(lines)-1)) * 0.15, line,
               ha='center', va='center', fontsize=9, fontweight='bold')

# Helper to draw data store (open rectangle on side)
def draw_store(x, y, label, w=2.2, h=1.2):
    # Left side open
    points = [
        (x-w/2, y-h/2),
        (x+w/2, y-h/2),
        (x+w/2, y+h/2),
        (x-w/2, y+h/2),
        (x-w/2, y+h/2-0.3),
        (x-w/2+0.2, y+h/2-0.3),
        (x-w/2+0.2, y-h/2+0.3),
        (x-w/2, y-h/2+0.3),
        (x-w/2, y-h/2)
    ]
    from matplotlib.patches import Polygon
    poly = Polygon(points, closed=True, facecolor=color_store,
                  edgecolor='black', linewidth=2)
    ax.add_patch(poly)
    ax.text(x, y, label, ha='center', va='center', 
           fontsize=9, fontweight='bold')

# Helper to draw data flow arrow
def draw_flow(x1, y1, x2, y2, label='', offset=0.2):
    # Calculate midpoint for label
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25,
                           color=color_flow, linewidth=1.8,
                           connectionstyle="arc3,rad=0.1")
    ax.add_patch(arrow)
    
    if label:
        # Offset label position
        label_x = mid_x + offset
        label_y = mid_y + offset
        ax.text(label_x, label_y, label, ha='center', va='center',
               fontsize=8, bbox=dict(boxstyle='round,pad=0.3', 
                                    facecolor='white', alpha=0.9,
                                    edgecolor='none'))

# ===== EXTERNAL ENTITIES =====
draw_external(2, 14, 'Guest')
draw_external(2, 11, 'Host')
draw_external(2, 8, 'Admin')
draw_external(20, 13, 'Payment\nGateway')
draw_external(20, 10, 'Email\nService')
draw_external(20, 7, 'Storage\n(Images)')

# ===== LEVEL 0 PROCESSES =====
# Top row - User processes
draw_process(6, 13.5, 'Authenticate\nUser')
draw_process(10, 13.5, 'Manage\nUser Profile')

# Middle row - Property & Booking processes
draw_process(6, 11, 'Manage\nProperties')
draw_process(10, 11, 'Process\nBookings')

# Bottom row - Support processes
draw_process(6, 8.5, 'Process\nPayments')
draw_process(10, 8.5, 'Handle\nReviews')
draw_process(14, 11, 'Send\nNotifications')
draw_process(14, 8.5, 'Admin\nManagement')

# ===== DATA STORES =====
# Left side stores
draw_store(6, 6, 'User\nDatabase')
draw_store(10, 6, 'Property\nDatabase')
draw_store(14, 6, 'Booking\nDatabase')

# Right side stores
draw_store(18, 13, 'Payment\nDatabase')
draw_store(18, 10, 'Review\nDatabase')
draw_store(18, 7, 'Image\nStorage')

# ===== DATA FLOWS FROM EXTERNAL ENTITIES TO PROCESSES =====

# Guest flows
draw_flow(4.5, 14, 5.15, 13.5, 'Login Credentials')
draw_flow(4.5, 14, 9.15, 13.5, 'Profile Updates')
draw_flow(4.5, 14, 5.15, 11, 'Property Search\nRequest')
draw_flow(4.5, 14, 9.15, 11, 'Booking Request')
draw_flow(4.5, 14, 11.15, 11, 'Booking\nModifications')
draw_flow(4.5, 14, 5.15, 8.5, 'Payment Info')
draw_flow(4.5, 14, 9.15, 8.5, 'Review Data')
draw_flow(4.5, 14, 13.15, 11, 'Message')

# Host flows
draw_flow(4.5, 11, 5.15, 11, 'Property Data')
draw_flow(4.5, 11, 9.15, 11, 'Booking\nResponses')
draw_flow(4.5, 11, 11.15, 11, 'Availability\nUpdates')
draw_flow(4.5, 11, 13.15, 8.5, 'Review Data')
draw_flow(4.5, 11, 13.15, 11, 'Message')

# Admin flows
draw_flow(4.5, 8, 13.15, 8.5, 'Moderation\nActions')

# Payment Gateway flows
draw_flow(17.85, 13, 11.15, 8.5, 'Payment\nConfirmation')
draw_flow(11.85, 8.5, 17.15, 13, 'Payment\nRequest')

# Email Service flows
draw_flow(13.85, 11, 17.15, 10, 'Notification\nData')
draw_flow(17.85, 10, 5.15, 13.5, 'Verification\nStatus')

# Storage flows
draw_flow(5.15, 11, 17.15, 7, 'Property\nImages')
draw_flow(17.85, 7, 5.15, 11, 'Image URLs')

# ===== DATA FLOWS FROM PROCESSES TO DATA STORES =====

# User Database flows
draw_flow(6, 12.75, 6, 7.2, 'User Data')
draw_flow(10, 12.75, 6, 7.2, 'Profile Updates', offset=-0.2)

# Property Database flows
draw_flow(6, 10.25, 10, 7.2, 'Property Data')
draw_flow(6, 10.25, 10, 7.2, 'Property\nUpdates', offset=0.4)

# Booking Database flows
draw_flow(10, 10.25, 14, 7.2, 'Booking Data')
draw_flow(10, 10.25, 14, 7.2, 'Booking\nStatus', offset=-0.4)

# Payment Database flows
draw_flow(6, 7.75, 18, 12.2, 'Payment Records')
draw_flow(6, 7.75, 18, 12.2, 'Transaction\nData', offset=0.3)

# Review Database flows
draw_flow(10, 7.75, 18, 9.2, 'Review Data')
draw_flow(10, 7.75, 18, 9.2, 'Ratings', offset=-0.3)

# Image Storage flows
draw_flow(6, 10.25, 18, 6.2, 'Image Files')

# ===== DATA FLOWS FROM DATA STORES TO PROCESSES =====

# From User Database
draw_flow(6, 6.8, 5.15, 13.5, 'User Info')
draw_flow(6, 6.8, 9.15, 13.5, 'Profile Data')

# From Property Database
draw_flow(10, 7.2, 5.15, 11, 'Property\nListings')
draw_flow(10, 7.2, 9.15, 11, 'Property\nDetails')

# From Booking Database
draw_flow(14, 7.2, 9.15, 11, 'Booking\nHistory')
draw_flow(14, 7.2, 13.15, 8.5, 'Booking\nInfo')

# From Payment Database
draw_flow(18, 12.2, 6, 8.5, 'Payment\nHistory')

# From Review Database
draw_flow(18, 9.2, 10, 8.5, 'Review\nData')

# From Image Storage
draw_flow(18, 6.8, 6, 11, 'Image URLs')
draw_flow(18, 6.8, 10, 11, 'Image URLs')

# ===== PROCESS TO PROCESS FLOWS =====
draw_flow(8.4, 13.5, 9.15, 13.5, 'User Auth', offset=-0.1)
draw_flow(6, 12, 9.15, 11.5, 'User\nVerification')
draw_flow(10, 11.5, 11.15, 8.5, 'Booking\nConfirmation')
draw_flow(10, 10.5, 11.15, 8.5, 'Payment\nRequired')
draw_flow(8.4, 8.5, 9.15, 8.5, 'Payment\nStatus')

# Title
ax.text(11, 15.5, 'Airbnb Clone Backend - Data Flow Diagram (Level 0)', 
        ha='center', va='top', fontsize=20, fontweight='bold')

# Legend
legend_elements = [
    mpatches.Patch(facecolor=color_external, edgecolor='black', 
                  label='External Entity', linewidth=2),
    mpatches.Patch(facecolor=color_process, edgecolor='#2c5aa0',
                  label='Process', linewidth=2),
    mpatches.Patch(facecolor=color_store, edgecolor='black',
                  label='Data Store', linewidth=2),
]

ax.legend(handles=legend_elements, loc='lower center', 
         bbox_to_anchor=(0.5, 0.01), ncol=3, fontsize=11, 
         framealpha=0.9, edgecolor='black')

# Footer
ax.text(11, 0.3, 'Data flows show movement of information through the system',
        ha='center', va='bottom', fontsize=10, style='italic', color='gray')

plt.tight_layout()
plt.savefig('data-flow-diagram/data-flow.png',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("Data Flow Diagram generated successfully: data-flow.png")
plt.close()

