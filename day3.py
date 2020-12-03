from functools import reduce
from operator import mul

def check_slope(map_lines, x_offset, y_offset):
    row_length = len(map_lines[0])
    x = 0
    trees_count = 0
    for row in map_lines[::y_offset]:
        trees_count += 1 if row[x] == '#' else 0
        x += x_offset
        x %= row_length
    return trees_count

def first(map_lines):
    return check_slope(map_lines, 3, 1)

def second(map_lines):
    slopes = [
        check_slope(map_lines, 1, 1),
        check_slope(map_lines, 3, 1),
        check_slope(map_lines, 5, 1),
        check_slope(map_lines, 7, 1),
        check_slope(map_lines, 1, 2)
    ]
    return reduce(mul, slopes, 1)