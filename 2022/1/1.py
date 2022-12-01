import os
PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines = []
    for line in file_in:
        try:
            lines.append(int(line))
        except ValueError:
            lines.append("")

idx = 0
elfs = []
acc = 0

while (idx < len(lines)):
    line = lines[idx]

    if (line == ""):
        elfs.append(acc)
        acc = 0
    else:
        acc += line

    idx += 1

print(max(elfs))
