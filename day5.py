from re import sub

def first(lines):
    seat_ids = [int(sub(r'B|R', '1', sub(r'F|L', '0', line)), 2) for line in lines]
    return max(seat_ids)

def second(lines):
    seat_ids = [int(sub(r'B|R', '1', sub(r'F|L', '0', line)), 2) for line in lines]
    missing_seats = set(range(2 ** 10)) - set(seat_ids)
    return next(seat for seat in missing_seats if seat - 1 not in missing_seats and seat + 1 not in missing_seats)