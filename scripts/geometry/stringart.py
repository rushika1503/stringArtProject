from .pinCircle import generate_pins
from .bresenhamLine import bresenham_line

pins = generate_pins(200, 400)

line_paths = {}

num_pins = len(pins)

for i in range(num_pins):
    for j in range(i + 1, num_pins):
        x0, y0 = pins[i]
        x1, y1 = pins[j]

        # Compute & store full pixel path
        pixel_list = bresenham_line(x0, y0, x1, y1)
        line_paths[(i, j)] = pixel_list

print("Total precomputed lines:", len(line_paths))
# Example:
first_key = next(iter(line_paths))
# print("Example line:", first_key)
# print("Pixel count:", len(line_paths[first_key]))
# print("First 10 pixels:", line_paths[first_key][:10])


# import matplotlib.pyplot as plt

# # plot a single line
# example_pixels = line_paths[first_key]

# xs = [p[0] for p in example_pixels]
# ys = [p[1] for p in example_pixels]

# plt.figure(figsize=(5,5))
# plt.scatter(xs, ys, s=3)
# plt.gca().invert_yaxis()
# plt.title(f"Line between pins {first_key}")
# plt.show()