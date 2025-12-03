import numpy as np
import matplotlib.pyplot as plt

def generate_pins(num_pins=200, canvas_size=400):
    # Determine the center point of the canvas
    center_x = canvas_size // 2
    center_y = canvas_size // 2

    # Radius for the circle on which all pins will be placed
    radius = canvas_size * 0.45

    # List to store pin coordinates
    pins = []

    # Compute pin coordinates on the circle
    for i in range(num_pins):
        angle = 2 * np.pi * (i / num_pins)
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        pins.append((int(x), int(y)))

    # Convert list to numpy array
    pins = np.array(pins)

    # Plot after computing all pins
    # plt.figure(figsize=(5,5))
    # plt.scatter(pins[:, 0], pins[:, 1], s=6, color='black')
    # plt.gca().invert_yaxis()
    # plt.title("String Art Pin Positions")
    # plt.axis('equal')
    # plt.show()

    return pins
