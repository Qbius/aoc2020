lines = list(map(int, open('inputs/day1.txt').readlines()))

def first():
    a, b = next((a, b) for a in lines for b in lines if a + b == 2020)
    print(f'First: {a * b}')

def second():
    a, b, c = next((a, b, c) for a in lines for b in lines for c in lines if a + b + c == 2020)
    print(f'First: {a * b * c}')

first()
second()