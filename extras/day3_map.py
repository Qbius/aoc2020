from re import findall
import numpy as np
from os.path import basename
from PIL import Image, ImageDraw

empty = (255, 255, 255)
tree = (0, 255, 0)
road = (0, 128, 255)
crash = (0, 0, 0)

lines = open('inputs/day3.txt').readlines()
width_coeff = round(len(lines) * 5 / len(lines[0]))
themap = [[empty if c == '.' else tree for c in list(line.strip())] * width_coeff for line in lines]
slopes = [
    [(0, 0), (1, 1)],
    [(0, 0), (3, 1)],
    [(0, 0), (5, 1)],
    [(0, 0), (7, 1)],
    [(0, 0), (1, 2)],
]


for i in range(len(themap)):
    for slope_index, ((curr_x, curr_y), (offset_x, offset_y)) in enumerate(slopes):
        if curr_y == i and curr_x < len(themap[i]):
            themap[i][curr_x] = road if themap[i][curr_x] == empty else crash
        slopes[slope_index] = ((curr_x + offset_x, curr_y + offset_y), (offset_x, offset_y))

img = Image.fromarray(np.array(themap, np.uint8))
img.save(f"extras/{basename(__file__).split('.')[0]}.png")