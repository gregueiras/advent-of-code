from typing import List
import os
from pprint import pprint
from math import floor, log10

PATH = os.path.join(os.path.dirname(__file__), "input.txt")
possible_operations = ["*", "+", "||"]


def calc(numbers, operations):
    num = numbers.copy()
    n_operations = len(operations)

    num = num[: n_operations + 1]

    acc = num[0]
    idx = 1
    for op in operations:
        if op == "+":
            acc += num[idx]
        elif op == "*":
            acc *= num[idx]
        elif op == "||":
            acc = int(str(acc) + str(num[idx]))

        idx += 1

    return acc


def resolve(target, numbers):
    ans = []

    def backtrack(curr_comb):
        if len(ans) > 0:
            return

        if (len(curr_comb) == (len(numbers) - 1)) and calc(numbers, curr_comb) == target:
            ans.append(curr_comb.copy())  # copying into the main list
            return

        elif (len(curr_comb) == (len(numbers) - 1)) or calc(
            numbers, curr_comb
        ) > target:
            return  # stop going down the path if sum greater than target

        for possible_op in possible_operations:
            curr_comb.append(possible_op)
            backtrack(curr_comb)
            curr_comb.pop()

    backtrack([])
    return ans


with open(PATH) as file_in:
    rows = []

    for line in file_in:
        try:
            line = line.strip()
            sp = line.split(":")
            rows.append((int(sp[0]), list(map(int, sp[1].split()))))

        except ValueError:
            pass

    acc = 0

    for row in rows:
        target = row[0]
        numbers = row[1]

        res = resolve(target, numbers)
        if len(res) > 0:
            acc += row[0]

    print(acc)
