import os
from traceback import print_tb

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def walk_up(guard_x, guard_y):
    while puzzle[guard_y][guard_x] != "#":
        puzzle[guard_y][guard_x] = "X"
        guard_y -= 1

        if guard_y < 0:
            return True

    puzzle[guard_y + 1][guard_x] = ">"

    return False

def walk_down(guard_x, guard_y):
    while puzzle[guard_y][guard_x] != "#":
        puzzle[guard_y][guard_x] = "X"
        guard_y += 1

        if guard_y > max_y:
            return True

    puzzle[guard_y - 1][guard_x] = "<"

    return False

def walk_left(guard_x, guard_y):
    while puzzle[guard_y][guard_x] != "#":
        puzzle[guard_y][guard_x] = "X"
        guard_x -= 1

        if guard_x < 0:
            return True

    puzzle[guard_y][guard_x + 1] = "^"

    return False

def walk_right(guard_x, guard_y):
    while puzzle[guard_y][guard_x] != "#":
        puzzle[guard_y][guard_x] = "X"
        guard_x += 1

        if guard_x > max_x:
            return True

    puzzle[guard_y][guard_x - 1] = "v"

    return False


def walk(puzzle):
    guard_x, guard_y = None, None

    guard_found = False
    for y in range(len(puzzle)):
        if guard_found:
            break
        for x in range(len(puzzle[0])):
            pos = puzzle[y][x]
            if pos in ["^", "<", ">", "v"]:
                guard_x = x
                guard_y = y
                guard_found = True
                break

    options = {
        "^": walk_up,
        "<": walk_left,
        ">": walk_right,
        "v": walk_down,
    }

    return options[pos](guard_x, guard_y)


with open(PATH) as file_in:
    puzzle = []

    for line in file_in:
        try:
            line = list(line.strip())
            puzzle.append(line)

        except ValueError:
            pass


    max_x = len(puzzle[0]) - 1
    max_y = len(puzzle) - 1


    while not walk(puzzle):
        pass

    acc = 0
    for line in puzzle:
        acc += sum(list(map(lambda x: x == "X", line)))
    
    print(acc)