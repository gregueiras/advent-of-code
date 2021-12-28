import os
from aux import Board

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        intLine =  [l[start:start+1] for start in range(len(l))]
        lines.append(intLine)

board = Board(lines)

board.steps(100)

print(board.flashes)