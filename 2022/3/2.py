import os
PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        lines.append(line.strip())

acc = 0
idx = 0

while idx < len(lines):
    first: "set[str]" = set(lines[idx])
    second: "set[str]" = set(lines[idx + 1])
    third: "set[str]" = set(lines[idx + 2])

    common = first.intersection(second).intersection(third).pop()
    priority = ord(common.lower()) - ord('a') + \
        1 + (26 if common.isupper() else 0)

    acc += priority

    idx += 3

print(acc)
