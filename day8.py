from common import regex
from copy import deepcopy

def run(tape, repeat_policy, check_for_halting=False):
    executed = set()
    state = {
        'acc': 0,
        'index': 0,
    }
    operations = {
        'jmp': lambda s, v: {**s, 'index': s['index'] + v},
        'acc': lambda s, v: {**s, 'index': s['index'] + 1, 'acc': s['acc'] + v},
        'nop': lambda s, v: {**s, 'index': s['index'] + 1},
    }
    while True:
        op, val = tape[state['index']]
        if repeat_policy(op, val):
            if state['index'] in executed:
                return None if check_for_halting else state['acc']
            else:
                executed.add(state['index'])
        state = operations[op](state, val)
        if state['index'] == len(tape):
            return state['acc']

def first(lines: regex(r'(nop|jmp|acc) ([+\-\d]+)', (str, int))):
    return run(lines, lambda _, __: True)

def second(lines: regex(r'(nop|jmp|acc) ([+\-\d]+)', (str, int))):
    nopjmp_indices = [i for i, (op, val) in enumerate(lines) if op == 'jmp' or op == 'nop']
    for nopjmp_index in nopjmp_indices:
        nopjmp_op, nopjmp_val = lines[nopjmp_index]
        tape = deepcopy(lines)
        tape[nopjmp_index] = ('jmp' if nopjmp_op == 'nop' else 'nop', nopjmp_val)
        result = run(tape, lambda op, _: op == 'jmp', check_for_halting=True)
        if result is not None:
            return result