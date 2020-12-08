from common import regex
from re import findall
from copy import deepcopy
from functools import reduce

def merge_dicts(a, b):
    common_keys = list(set(a.keys()) & set(b.keys()))
    common_dict = {key: a[key] + b[key] for key in common_keys}
    return {**a, **b, **common_dict}

def first(lines: regex(r'([a-z ]+) bags contain ([a-z\d ,]+)', (str, str))):
    bags_dict = {color: findall(r'\d+ ([a-z ]+) (?:bag|bags)', der_bags) for color, der_bags in lines}
    def contains_bag()
    to_find = {'shiny gold'}
    to_find_old = None
    while to_find != to_find_old:
        to_find_old = deepcopy(to_find)
        to_find = {color for color, der_bags in bags_dict.items() if any(der_color in der_bags for der_color in to_find_old)} | to_find_old
    return len(to_find - {'shiny gold'})
    
def second(lines: regex(r'([a-z ]+) bags contain ([a-z\d ,]+)', (str, str))):
    bags_dict = {color: [(der_color, int(number_str)) for number_str, der_color in findall(r'(\d+) ([a-z ]+) (?:bag|bags)', der_bags)] for color, der_bags in lines}
    def bag_count(color, count):
        return count * sum(bag_count(der_color, der_count) for der_color, der_count in bags_dict[color]) + count
    return bag_count('shiny gold', 1) - 1