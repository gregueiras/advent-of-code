import os
from math import floor

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        intLine = [l[start:start+1] for start in range(len(l))]
        lines.append(intLine)

chars = {
    '[': ']', '{': '}', '(': ')', '<': '>'
}
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

errors = []

for line in lines:
    stack = []
    isCorrupt = False
    for char in line:
        if char in chars.keys():
            stack.append(char)
        else:
            stackChar = stack.pop()
            if chars[stackChar] != char:
                isCorrupt = True
                break

    if not isCorrupt:
        acc = 0
        closes = ''
        for char in reversed(stack):
            closer = chars[char]
            closes += closer
            point = points[closer]
            acc = acc * 5 + point

        errors.append(acc)

print(errors)

errors.sort()


midIdx = floor(len(errors) / 2)
print(errors[midIdx])
