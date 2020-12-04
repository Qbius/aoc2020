from functools import reduce
from operator import mul

def check_slope(map_lines, x_offset, y_offset):
    return len([line for i, line in enumerate(map_lines[::y_offset]) if line[(i * x_offset) % len(line)] == '#'])

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