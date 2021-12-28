from aux import Board
from pathlib import Path

path = Path(__file__).parent / "./input.txt"

dots = []
instructions = []

readingDots = True
with open(path) as fp:
    Lines = fp.readlines()
    for line in Lines:
        line = line.strip()
        if line == "":
            readingDots = False
        elif readingDots:
            dots.append(list(map(int, line.split(","))))
        elif not readingDots:
            inst = line.split("=")
            instructions.append((inst[0][-1], int(inst[1])))

board = Board(dots, instructions)

# board.instructions.reverse()

for inst in board.instructions:
    board.fold(inst)

# print(board._printBoard(board.board))
print(board.visible())

print(board.visible())
print(board.dimX)
print(board.dimY)
print(len(board.board))
