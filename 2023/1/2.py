import os

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open(PATH) as file_in:
    lines = []
    for line in file_in:
        try:
            lines.append(line.strip())
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

        shouldBreak = False
        for numString, numValue in digits.items():
            try:
                if line[idx : idx + len(numString)] == numString:
                    digit1 = numValue
                    shouldBreak = True
                    break
            except:
                pass

        if shouldBreak:
            break

    for idx in range(len(line) - 1, -1, -1):
        try:
            digit2 = int(line[idx])
            break
        except:
            pass

        shouldBreak = False
        for numString, numValue in digits.items():
            try:
                if line[idx - len(numString) + 1 : idx + 1] == numString:
                    digit2 = numValue
                    shouldBreak = True
                    break
            except:
                pass

        if shouldBreak:
            break

    if digit1 is not None and digit2 is not None:
        acc += digit1 * 10 + digit2

print(acc)
