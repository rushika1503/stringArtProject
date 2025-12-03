🎨 String Art Generator (Python)

Convert any uploaded image into generative string art using image processing, geometry, and line–by–line optimization.

🚀 Project Status (Current Progress)

You have completed the following major components:

✔️ 1. Image Preprocessing

Resize image to fixed resolution

Convert to grayscale

Normalize brightness values

Optional contrast boost

✔️ 2. Pin Generation

Create evenly spaced pins around a perfect circle

Customizable number of pins

Produces (x, y) coordinates for each pin

Visual debugging via matplotlib scatter plot

✔️ 3. Line Pixel Path Generation (Bresenham)

Implemented Bresenham’s Line Algorithm

Precompute pixel paths for all pin pairs
 
Stored in dictionary: line_paths[(i, j)] → [(x1,y1), (x2,y2), …]
