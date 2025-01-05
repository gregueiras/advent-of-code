from typing import List
import os
from pprint import pprint
from math import floor, log10

PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")

visited = set()
groups = {}


def inside(x, y):
    return (x, y) in visited


def area(group: list[tuple[int, int]]) -> int:
    return len(group)


def perimeter(group: list[tuple[int, int]]) -> int:
    if len(group) == 1:
        return 4

    max_x = max(map(lambda coord: coord[0], group))
    min_x = min(map(lambda coord: coord[0], group))

    max_y = max(map(lambda coord: coord[1], group))
    min_y = min(map(lambda coord: coord[1], group))

    return 2 * ((1 + max_x - min_x) + (1 + max_y - min_y))


def fill(puzzle, x, y):
    if not inside(x, y):
        return

    s = []
    s.append((x, x, y, 1))
    s.append((x, x, y - 1, -1))

    while len(s) > 0:
        x1, x2, y, dy = s.pop()

        x = x1
        if inside(x, y):
            while inside(x - 1, y):
                visited.add((x - 1, y))
                group = puzzle[y][x - 1]
                groups[group] = groups.get(group, []) + [(x, y)]
                x = x - 1
            if x < x1:
                s.append((x, x1 - 1, y - dy, -dy))
        while x1 <= x2:
            while inside(x1, y):
                visited.add((x1, y))
                group = puzzle[y][x1]
                groups[group] = groups.get(group, []) + [(x1, y)]
                x1 = x1 + 1
            if x1 > x:
                s.append((x, x1 - 1, y + dy, dy))
            if x1 - 1 > x2:
                s.append((x2 + 1, x1 - 1, y - dy, -dy))
            x1 = x1 + 1
            while x1 < x2 and not inside(x1, y):
                x1 = x1 + 1
            x = x1

    ans = []

    def backtrack(curr_path, actual_coords):
        if is_finished(curr_path, puzzle, ans):
            ans.append(curr_path.copy())  # copying into the main list
            return

        for possible_next in get_possible_next(puzzle, actual_coords):
            curr_path.append(possible_next)
            backtrack(curr_path, possible_next)
            curr_path.pop()

    all_answers = []

    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            pos = puzzle[y][x]
            if pos == "0":
                backtrack([], (x, y))
                all_answers.extend(ans)
                ans.clear()

    return all_answers


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
            visited.add((x, y))

    fill(puzzle, 0, 0)
    pprint(groups)

    acc = 0

    for group, coords in groups.items():
        _area = area(coords)
        _perimeter = perimeter(coords)

        print(f"{group} {_area}, {_perimeter}")
        acc += _area * _perimeter

    print(acc)
