from re import findall
from math import sqrt, ceil
from os.path import basename
from PIL import Image, ImageDraw

cell_width = 30
cell_height = 10

hair_colors = findall(r'hcl:(#[0-9a-f]{6})', open('inputs/day4.txt').read())

rows_count = ceil(sqrt(len(hair_colors)))
width = rows_count * cell_width

columns_count = ceil(len(hair_colors) / rows_count)
height = columns_count * cell_height
print(width, height)

colors_and_coords = [(color, ((i * cell_width) % width, i // rows_count * cell_height)) for i, color in enumerate(hair_colors)]

img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)
for color, coords in colors_and_coords:
    x, y = coords
    draw.rectangle([coords, (x + cell_width, y + cell_height)], fill=color)
img.save(f"extras/{basename(__file__).split('.')[0]}.png")