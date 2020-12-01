def first(lines: int):
    a, b = next((a, b) for a in lines for b in lines if a + b == 2020)
    return a * b

def second(lines: int):
    a, b, c = next((a, b, c) for a in lines for b in lines for c in lines if a + b + c == 2020)
    return a * b * c