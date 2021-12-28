import os
from statistics import mode

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

def calc(target: int) -> int:
    acc = 0
    for crab in crabs:
        acc += abs(crab - target)

    return acc


crabs = list(map(int, lines[0].split(",")))

print(crabs)
print(calc(mode(crabs)))

