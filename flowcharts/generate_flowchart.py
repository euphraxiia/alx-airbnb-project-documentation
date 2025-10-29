#!/usr/bin/env python3
"""
Generate a Flowchart for Property Booking Process
Shows the complete workflow from search to booking confirmation
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.patches as mpatches

fig, ax = plt.subplots(1, 1, figsize=(18, 24))
ax.set_xlim(0, 14)
ax.set_ylim(0, 24)
ax.axis('off')

# Define colors
color_process = '#E8F4F8'  # Light blue for process boxes
color_decision = '#FFE5B4'  # Peach for decision diamonds
color_terminal = '#90EE90'  # Light green for start/end
color_data = '#F0E68C'    # Khaki for data/document steps
color_note = '#DDA0DD'    # Plum for note boxes

# Helper to draw process/operation (rectangle)
def draw_process(x, y, label, w=2.5, h=0.8):
    box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                        boxstyle="round,pad=0.1",
                        facecolor=color_process,
                        edgecolor='#2c5aa0',
                        linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', 
           fontsize=9, fontweight='bold', wrap=True)

# Helper to draw decision (diamond)
def draw_decision(x, y, label, size=0.8):
    from matplotlib.patches import RegularPolygon
    diamond = RegularPolygon((x, y), 4, radius=size, 
                            orientation=0.785398,
                            facecolor=color_decision,
                            edgecolor='#FF8C00',
                            linewidth=2)
    ax.add_patch(diamond)
    ax.text(x, y, label, ha='center', va='center', 
           fontsize=8, fontweight='bold')

# Helper to draw terminal (rounded rectangle)
def draw_terminal(x, y, label, w=2.2, h=0.7):
    box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                        boxstyle="round,pad=0.15",
                        facecolor=color_terminal,
                        edgecolor='#008000',
                        linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', 
           fontsize=9, fontweight='bold')

# Helper to draw data/document (parallelogram)
def draw_data(x, y, label, w=2.5, h=0.8):
    points = [
        (x-w/2+0.2, y-h/2),
        (x+w/2, y-h/2),
        (x+w/2-0.2, y+h/2),
        (x-w/2, y+h/2)
    ]
    from matplotlib.patches import Polygon
    poly = Polygon(points, closed=True, 
                  facecolor=color_data,
                  edgecolor='#8B6914',
                  linewidth=2)
    ax.add_patch(poly)
    ax.text(x, y, label, ha='center', va='center', 
           fontsize=8, fontweight='bold')

# Helper to draw arrow
def draw_arrow(x1, y1, x2, y2, label='', offset_x=0, offset_y=0.15):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=20,
                           color='#333333', linewidth=1.8)
    ax.add_patch(arrow)
    
    if label:
        mid_x = (x1 + x2) / 2 + offset_x
        mid_y = (y1 + y2) / 2 + offset_y
        ax.text(mid_x, mid_y, label, ha='center', va='center',
               fontsize=7, style='italic',
               bbox=dict(boxstyle='round,pad=0.2', 
                        facecolor='white', alpha=0.9,
                        edgecolor='none'))

# Title
ax.text(7, 23.5, 'Property Booking Process Flowchart', 
        ha='center', va='top', fontsize=18, fontweight='bold')

# ===== FLOWCHART ELEMENTS =====

# Start
draw_terminal(7, 22.5, 'START')

# Guest searches for properties
draw_process(7, 21.5, 'Guest searches\nfor properties')

# Display search results
draw_data(7, 20.5, 'Display search\nresults')

# Select property
draw_process(7, 19.5, 'Guest selects\nproperty')

# View property details
draw_data(7, 18.5, 'View property\ndetails')

# Check if logged in
draw_decision(7, 17.5, 'User\nlogged in?')

# If not logged in, login/register
draw_process(4, 16.5, 'Login or\nRegister')
draw_arrow(6.2, 17.5, 4, 17.2)

# After login, return to property
draw_process(4, 15.5, 'Return to\nproperty page')
draw_arrow(4, 16.2, 4, 15.8)

# Select dates and guests
draw_process(7, 16.5, 'Select dates\nand guests')

# Check availability
draw_process(7, 15.5, 'Check property\navailability')

# Decision: Available?
draw_decision(7, 14.5, 'Property\navailable?')

# If not available, show message
draw_process(4, 13.5, 'Show not available\nmessage')
draw_arrow(6.2, 14.5, 4, 14.2)

# Return to search
draw_process(4, 12.5, 'Return to\nsearch')
draw_arrow(4, 13.2, 4, 12.8)

# Calculate price
draw_process(10, 14.5, 'Calculate total\nprice')

# Show booking summary
draw_data(10, 13.5, 'Display booking\nsummary')

# Review booking details
draw_process(10, 12.5, 'Guest reviews\nbooking details')

# Decision: Proceed?
draw_decision(10, 11.5, 'Proceed to\npayment?')

# If no, back to modify
draw_process(7.5, 10.5, 'Modify booking\ndetails')
draw_arrow(9.2, 11.5, 8.5, 11.2)

# Return to date selection
draw_arrow(7.5, 10.2, 7, 16.8, 'Back')

# If yes, enter payment info
draw_process(12.5, 11.5, 'Enter payment\ninformation')
draw_arrow(10.8, 11.5, 12.5, 11.5, 'Yes')

# Validate payment
draw_process(12.5, 10.5, 'Validate payment\ndetails')

# Decision: Payment valid?
draw_decision(12.5, 9.5, 'Payment\nvalid?')

# If invalid, show error
draw_process(10, 8.5, 'Show payment\nerror')
draw_arrow(11.7, 9.5, 10.5, 9.2)

# Return to payment
draw_arrow(10, 8.2, 12.5, 11.2, 'Retry')

# If valid, process payment
draw_process(12.5, 8.5, 'Process payment\nwith gateway')
draw_arrow(12.5, 9.2, 12.5, 9.0)

# Decision: Payment successful?
draw_decision(12.5, 7.5, 'Payment\nsuccessful?')

# If failed
draw_process(10, 6.5, 'Payment failed\nhandle error')
draw_arrow(11.7, 7.5, 10.5, 7.2)

# Notify guest
draw_process(10, 5.5, 'Notify guest\nof failure')
draw_arrow(10, 6.2, 10, 6.0)

# End (failed)
draw_terminal(10, 4.5, 'END\n(Booking Failed)')

# If successful, create booking
draw_process(15, 7.5, 'Create booking\nrecord')
draw_arrow(13.3, 7.5, 15, 7.5, 'Yes')

# Update property availability
draw_process(15, 6.5, 'Update property\navailability')

# Save booking to database
draw_data(15, 5.5, 'Save booking to\ndatabase')

# Send confirmation email
draw_process(15, 4.5, 'Send confirmation\nemail')

# Create invoice
draw_data(15, 3.5, 'Generate booking\ninvoice')

# Notify host
draw_process(15, 2.5, 'Notify host of\nnew booking')

# Update booking status
draw_process(15, 1.5, 'Set booking status\nto "Confirmed"')

# Display success message
draw_process(15, 0.5, 'Display booking\nconfirmation')

# End (success)
draw_terminal(15, -0.5, 'END\n(Booking Confirmed)')

# Connect login flow back
draw_arrow(4, 15.2, 7, 16.8)

# Connect not available back
draw_arrow(4, 12.2, 7, 20.8, 'Search again')

# Connect modify back
draw_arrow(7.5, 10.2, 7, 16.8)

# Legend
legend_x = 0.5
legend_y = 11
legend_elements = [
    mpatches.Patch(facecolor=color_terminal, edgecolor='#008000',
                  label='Start/End', linewidth=2),
    mpatches.Patch(facecolor=color_process, edgecolor='#2c5aa0',
                  label='Process', linewidth=2),
    mpatches.Patch(facecolor=color_decision, edgecolor='#FF8C00',
                  label='Decision', linewidth=2),
    mpatches.Patch(facecolor=color_data, edgecolor='#8B6914',
                  label='Data/Document', linewidth=2),
]

ax.legend(handles=legend_elements, loc='upper left', 
         bbox_to_anchor=(0.01, 0.99), fontsize=10, 
         framealpha=0.9, edgecolor='black', title='Flowchart Symbols')

# Footer note
ax.text(7, -1.5, 'This flowchart illustrates the complete property booking workflow from search to confirmation',
        ha='center', va='top', fontsize=9, style='italic', color='gray')

plt.tight_layout()
plt.savefig('flowcharts/data-flow-diagram.png',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("Property Booking Flowchart generated successfully: data-flow-diagram.png")
plt.close()

