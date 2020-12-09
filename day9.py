def has_numbers_that_sum_up(value, numbers):
    numbers.sort()
    first = 0
    last = len(numbers) - 1
    while first < last:
        currsum = numbers[first] + numbers[last]
        if currsum < value:
            first += 1
        elif currsum > value:
            last -= 1
        else:
            return True
    return False

def first(lines: int):
    return next(lines[i] for i in range(29, len(lines)) if not has_numbers_that_sum_up(lines[i], lines[i - 25:i]))

def second(lines: int):
    sought = first(lines)
    for size in range(2, len(lines) + 1):
        if contiguous_sets := [(i, size) for i in range(0, len(lines) - size) if sum(lines[i:i + size]) == sought]:
            i, size = contiguous_sets[0]  
            return min(lines[i:i + size]) + max(lines[i:i + size])
    