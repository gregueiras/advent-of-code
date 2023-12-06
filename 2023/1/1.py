import os
PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines = []
    for line in file_in:
        try:
            lines.append(line)
        except ValueError:
            lines.append("")

acc = 0

for line in lines:
    digit1, digit2 = None, None

    for idx in range(0, len(line)):
        try:
            digit1 = int(line[idx])
            break
        except:
            pass

    for idx in range(len(line) - 1, -1, -1):
        try:
            digit2 = int(line[idx])
            break
        except:
            pass


    if digit1 is not None and digit2 is not None:
        acc += digit1 * 10 + digit2

print(acc)

