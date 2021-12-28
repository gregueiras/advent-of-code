from pathlib import Path


def print_board():
    dimX, dimY = [max(p[i] for p in board) for i in range(2)]

    for j in range(dimY + 1):
        for i in range(dimX + 1):
            print("#" if (i, j) in board else ".", end="")

        print("\n", end="")

    print("\n", end="")


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


board = set()

for dot in dots:
    board.add((dot[0], dot[1]))

# print_board()

for inst in instructions:
    new_board = set()
    axis = inst[0]
    foldPoint = inst[1]

    coordsIndex = 1 if axis == "y" else 0
    for p in board:
        coords = list(p)
        if coords[coordsIndex] > foldPoint:
            coords[coordsIndex] -= 2 * (coords[coordsIndex] - foldPoint)

        new_board.add((coords[0], coords[1]))

    board = new_board

print_board()
