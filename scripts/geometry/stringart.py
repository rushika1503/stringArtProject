from .pinCircle import generate_pins


pins = generate_pins(200,400)

line_paths = {}

print(pins)
num_pins = len(pins)
for i in range(num_pins):
    for j in range(i+1, num_pins):
        x0,y0 = pins[i]
        x1,y1 = pins[j]
        # print(x0,y0, x1,y1) 

