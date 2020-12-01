from sys import argv
from typing import get_type_hints
name = f'day{argv[1]}'
notimpl = lambda _: 'not implemented'

day_module = __import__(name)
day_input = open(f'inputs/{name}.txt').readlines()
day_first = getattr(day_module, 'first', notimpl)
day_second = getattr(day_module, 'second', notimpl)
day_first_arg = list(map(day_first_type_hints[0], day_input)) if (day_first_type_hints := list(get_type_hints(day_first).values())) else day_input
day_second_arg = list(map(day_second_type_hints[0], day_input)) if (day_second_type_hints := list(get_type_hints(day_second).values())) else day_input
print('First:', day_first(day_first_arg))
print('First:', day_second(day_second_arg))