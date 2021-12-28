import os
from statistics import median, mean
from math import ceil, floor

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

def calc_score(target: int) -> int:
    acc = 0
    for crab in crabs:
        distance = abs(crab - target) 
        acc += sum([i + 1 for i in range(distance)])

    return acc


crabs = list(map(int, lines[0].split(",")))

avg = mean(crabs)

print(f"Avg: {avg} {round(avg)} {ceil(avg)} {floor(avg)}")

print(calc_score(floor(avg)))
