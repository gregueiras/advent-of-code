import os
PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        lines.append(line.strip())

acc = 0

for line in lines:
    size = int(len(line) / 2)
    first: "set[str]" = set(line[size:])
    second: "set[str]" = set(line[:size])

    common = first.intersection(second).pop()
    priority = ord(common.lower()) - ord('a') + \
        1 + (26 if common.isupper() else 0)

    acc += priority

print(acc)
