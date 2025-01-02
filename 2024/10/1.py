from typing import List
import os
from pprint import pprint
from math import floor, log10

PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def is_finished(path, puzzle, answers):
    if len(path) != 9:
        return False
    
    for idx in range(len(path)):
        x, y = path[idx]
        pos = puzzle[y][x]

        if str(idx + 1) != pos:
            return False
        
    for answer in answers:
        if answer[-1] == path[-1]:
            return False

    return True


def get_possible_next(puzzle, actual_coords):
    x, y = actual_coords
    new_pos = str(int(puzzle[y][x]) + 1)

    possible_next = []
    if x > 0 and puzzle[y][x - 1] == new_pos:
        possible_next.append((x - 1, y))
    if x + 1 < len(puzzle[0]) and puzzle[y][x + 1] == new_pos:
        possible_next.append((x + 1, y))
    if y > 0 and puzzle[y - 1][x] == new_pos:
        possible_next.append((x, y - 1))
    if y + 1 < len(puzzle) and puzzle[y + 1][x] == new_pos:
        possible_next.append((x, y + 1))

    return possible_next


def resolve(puzzle):
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
            puzzle.append(line)
        except ValueError:
            pass

    ans = resolve(puzzle)

    print(len(ans))
