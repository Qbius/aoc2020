from itertools import groupby
from re import search, match

def first(lines):
    passports = [' '.join(list(group)).split(' ') for k, group in groupby(lines, lambda ele: ele == '') if not k]
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = [passport for passport in passports if all(any(part.startswith(field) for part in passport) for field in fields)]
    return len(valid_passports)

def second(lines):
    passports = [' '.join(list(group)).split(' ') for k, group in groupby(lines, lambda ele: ele == '') if not k]

    def check_height(val):
        matched = search(r'(\d+)(cm|in)', val)
        if not matched: return False
        value_str, unit = matched.groups()
        value = int(value_str)
        return (unit == 'cm' and value >= 150 and value <= 193) or (unit == 'in' and value >= 59 and value <= 76)

    checks = [
        ('byr', lambda val: val.isdigit() and len(val) == 4 and int(val) >= 1920 and int(val) <= 2002),
        ('iyr', lambda val: val.isdigit() and len(val) == 4 and int(val) >= 2010 and int(val) <= 2020),
        ('eyr', lambda val: val.isdigit() and len(val) == 4 and int(val) >= 2020 and int(val) <= 2030),
        ('hgt', check_height),
        ('hcl', lambda val: match(r'#[0-9a-f]{6}', val)),
        ('ecl', lambda val: val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        ('pid', lambda val: val.isdigit() and len(val) == 9),
    ]
    valid_passports = [passport for passport in passports if all(any(part.startswith(field) and check(part.split(':')[1]) for part in passport) for field, check in checks)]
    return len(valid_passports)
