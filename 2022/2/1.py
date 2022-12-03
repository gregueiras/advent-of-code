import os
PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

acc = 0

shapes = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

own_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

equivalent = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

win = 6
draw = 3
lose = 0

for line in lines:
    mine = line[2]
    their = line[0]

    if equivalent[their] == mine:
        acc += draw
    elif shapes[their] == mine:
        acc += win
    else:
        acc += lose

    acc += own_scores[mine]

print(acc)
