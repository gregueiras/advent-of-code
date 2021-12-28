import os
from aux import Board
from math import prod

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        intLine =  [l[start:start+1] for start in range(len(l))]
        lines.append(intLine)

board = Board(lines)
basins = board.findBasin()

sortedBasins = sorted(list(map(len, basins)))
top3 = sortedBasins[-3:]

print(prod(top3))


