import os

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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
errors = 0


for line in lines:
    stack = []
    for char in line:
        if char in chars.keys():
            stack.append(char)
        else:
            stackChar = stack.pop()
            if chars[stackChar] != char:
                errors += points[char]
                break

print(errors)
