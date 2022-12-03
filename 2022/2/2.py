import os
PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

acc = 0

to_win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

to_draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

to_lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

own_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

win = 6
draw = 3
lose = 0

for line in lines:
    instruction = line[2]
    their = line[0]

    if instruction == 'X':
        mine = to_lose[their]
        acc += lose
    elif instruction == 'Y':
        mine = to_draw[their]
        acc += draw
    else:
        mine = to_win[their]
        acc += win

    acc += own_scores[mine]

print(acc)
