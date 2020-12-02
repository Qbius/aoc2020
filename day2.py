from common import regex

def first(lines: regex(r'(\d+)-(\d+) (.): ([a-z]+)', (int, int, str, str))):
    return len([None for lower_str, upper_str, character, password in lines if password.count(character) >= lower_str and password.count(character) <= upper_str])

def second(lines: regex(r'(\d+)-(\d+) (.): ([a-z]+)', (int, int, str, str))):
    return len([None for first_pos, second_pos, character, password in lines if (password[first_pos - 1] == character) != (password[second_pos - 1] == character)])
