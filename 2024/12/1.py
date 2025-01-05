from typing import List
import os
from pprint import pprint
from math import floor, log10

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

global_to_visit = set()


def first_in_set(s):
    for e in s:
        break
    return e


def walk(puzzle, start_x, start_y):
    max_x = len(puzzle[0])
    max_y = len(puzzle)

    def look(x, y, dx, dy):
        if 0 <= x + dx < max_x and 0 <= y + dy < max_y:
            new_x = x + dx
            new_y = y + dy

            return (puzzle[new_y][new_x], (new_x, new_y))

        return (None, None)

    def look_up(x, y):
        return look(x, y, 0, -1)

    def look_down(x, y):
        return look(x, y, 0, 1)

    def look_right(x, y):
        return look(x, y, 1, 0)

    def look_left(x, y):
        return look(x, y, -1, 0)

    looks = [
        look_up,
        look_down,
        look_right,
        look_left,
    ]

    curr_group = puzzle[start_y][start_x]

    acc_perimeter = 0
    acc_area = 0

    group_to_visit = set()

    group_to_visit.add((start_x, start_y))

    while len(group_to_visit) > 0:
        x, y = group_to_visit.pop()

        new_group = puzzle[y][x]
        if new_group != curr_group:
            continue

        global_to_visit.remove((x, y))
        acc_area += 1

        for _look in looks:
            new_group, new_coords = _look(x, y)

            if new_group == curr_group:
                if new_coords in global_to_visit:
                    group_to_visit.add(new_coords)
            else:
                acc_perimeter += 1

    return acc_area, acc_perimeter


with open(PATH) as file_in:
    puzzle = []

    for line in file_in:
        try:
            line = line.strip()
            puzzle.append(list(line))
        except ValueError:
            pass

    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            global_to_visit.add((x, y))

    acc = 0

    while len(global_to_visit) > 0:
        x, y = first_in_set(global_to_visit)
        area, perimeter = walk(puzzle, x, y)

        print(f"{puzzle[y][x]} {area}, {perimeter}")
        acc += area * perimeter

    print(acc)
