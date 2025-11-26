import numpy as py
import matplotlib.pyplot as plt

def generate_pins(num_pins=200, canvas_size=400):
    # Determine the center point of the canvas
    center_x = canvas_size // 2
    center_y = canvas_size // 2

    # Radius for the circle on which all pins will be placed
    # Using 45% of canvas size keeps the circle inside the edges
    radius = canvas_size * 0.45

    # List that will store all (x, y) pin coordinates
    pins = []

    # Loop through each pin index and compute its position on the circle
    for i in range(num_pins):
        # Calculate angle for the current pin (in radians)
        angle = 2 * py.pi * (i / num_pins)

        # Convert polar coordinates → Cartesian coordinates
        x = center_x + radius * py.cos(angle)
        y = center_y + radius * py.sin(angle)

        # Add pin (rounded to nearest pixel)
        pins.append((int(x), int(y)))

    # Convert list to a NumPy array for easy manipulation
    return py.array(pins)


# # Plot circle of pins
# plt.figure(figsize=(5,5))
# plt.scatter(pins[:,0], pins[:,1], s=6, color='black')   # pins
# plt.gca().invert_yaxis()                                # image coordinates
# plt.title("String Art Pin Positions")
# plt.axis('equal')
# plt.show()