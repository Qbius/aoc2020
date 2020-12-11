from itertools import groupby
from functools import reduce
from operator import mul

def first(lines: int):
    srt = [0] + sorted(lines) + [max(lines) + 3]
    diffs = [srt[i] - srt[i - 1] for i in range(1, len(srt))]
    print(diffs)
    return diffs.count(1) * diffs.count(3)

def second(lines: int):
    srt = [0] + sorted(lines) + [max(lines) + 3]
    diffs = [srt[i] - srt[i - 1] for i in range(1, len(srt))]
    triangle_number = lambda n: n * (n + 1) // 2
    return reduce(mul, [triangle_number(len(list(group)) - 1) + 1 for k, group in groupby(diffs, lambda ele: ele == 3) if not k])
    