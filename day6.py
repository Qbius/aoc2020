from itertools import groupby

def first(lines):
    return sum([len(set(''.join(list(group)))) for k, group in groupby(lines, lambda ele: ele == '') if not k])

def second(lines):
    answers_lists = [list(group) for k, group in groupby(lines, lambda ele: ele == '') if not k]
    sheets_to_count = [(''.join(answers), len(answers)) for answers in answers_lists]
    return sum([len(set([c for c in answersheet if answersheet.count(c) == count])) for answersheet, count in sheets_to_count])