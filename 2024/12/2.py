from typing import List
import os
from pprint import pprint
from math import floor, log10
from functools import cmp_to_key

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

global_to_visit = set()


def first_in_set(s):
    for e in s:
        break
    return e


def walk(puzzle, start_x, start_y):
    max_x = len(puzzle[0])
    max_y = len(puzzle)

    def look(x, y, dx, dy, is_vertical, is_left_down):
        new_x = x + dx
        new_y = y + dy
        new_coords = (new_x, new_y)
        if 0 <= x + dx < max_x and 0 <= y + dy < max_y:

            return (puzzle[new_y][new_x], new_coords, is_vertical, is_left_down)

        return (None, new_coords, is_vertical, is_left_down)

    def look_up(x, y):
        return look(x, y, 0, -1, True, False)

    def look_down(x, y):
        return look(x, y, 0, 1, True, True)

    def look_right(x, y):
        return look(x, y, 1, 0, False, False)

    def look_left(x, y):
        return look(x, y, -1, 0, False, True)

    looks = [
        look_up,
        look_down,
        look_right,
        look_left,
    ]

    curr_group = puzzle[start_y][start_x]

    acc_perimeter_vertical = ([], [])
    acc_perimeter_horizontal = ([], [])
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
            new_group, new_coords, is_vertical, is_left_down = _look(x, y)
            idx = 0 if is_left_down else 1

            if new_group == curr_group:
                if new_coords in global_to_visit:
                    group_to_visit.add(new_coords)
            else:
                if is_vertical:
                    acc_perimeter_horizontal[idx].append(new_coords)
                else:
                    acc_perimeter_vertical[idx].append(new_coords)

    return acc_area, acc_perimeter_horizontal, acc_perimeter_vertical


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
    ans = []

    while len(global_to_visit) > 0:
        x, y = first_in_set(global_to_visit)
        area, perimeter_horizontal, perimeter_vertical = walk(puzzle, x, y)

        def countVertical(fences: List[tuple[int, int]]):
            def cmp_items(a, b):
                if a[0] == b[0]:
                    return a[1] - b[1]
                return a[0] - b[0]

            acc = 1
            fences.sort(key=cmp_to_key(cmp_items))
            old_fence = fences[0]

            for fence in fences[1:]:
                is_continuation = (
                    old_fence[1] == fence[1] - 1 and old_fence[0] == fence[0]
                )
                if not is_continuation:
                    acc += 1
                old_fence = fence

            return acc

        def countHorizontal(fences: List[tuple[int, int]]):
            def cmp_items(a, b):
                if a[1] == b[1]:
                    return a[0] - b[0]
                return a[1] - b[1]

            acc = 1
            fences.sort(key=cmp_to_key(cmp_items))
            old_fence = fences[0]

            for fence in fences[1:]:
                is_continuation = (
                    old_fence[0] == fence[0] - 1 and old_fence[1] == fence[1]
                )
                if not is_continuation:
                    acc += 1
                old_fence = fence

            return acc

        acc_perimeter_horizontal = countHorizontal(
            perimeter_horizontal[0]
        ) + countHorizontal(perimeter_horizontal[1])
        acc_perimeter_vertical = countVertical(perimeter_vertical[0]) + countVertical(
            perimeter_vertical[1]
        )

        acc_perimeter = acc_perimeter_horizontal + acc_perimeter_vertical

        print(
            "{ crop: '"
            + puzzle[y][x]
            + "', area: "
            + str(area)
            + ", sides: "
            + str(acc_perimeter)
            + " }"
        )

        acc += area * acc_perimeter

    print(acc)
