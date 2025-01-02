from typing import List
import os
from pprint import pprint
from math import floor, perm
import itertools

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def is_correct_order(update: List[str]) -> bool:
    for idx in range(len(update)):
        page = update[idx]

        if page in rules:
            afters = rules[page]
            prefix = update[:idx]

            for after in afters:
                if after in prefix:
                    return False

    return True


def fix_order(update: List[str]) -> List[str]:
    for idx in range(len(update)):
        page = update[idx]

        if page in rules:
            afters = rules[page]
            prefix = update[:idx]

            for after in afters:
                if after in prefix:
                    idx_after = update.index(after)
                    update[idx] = after
                    update[idx_after] = page
                    break

    return update


with open(PATH) as file_in:
    rules = {}
    updates = []

    is_rules = True

    for line in file_in:
        try:
            line = line.strip()
            if line == "":
                is_rules = False
                continue

            if is_rules:
                line = line.split("|")

                before = line[0]
                after = line[1]

                if before in rules:
                    rules[before].append(after)
                else:
                    rules[before] = [after]
            else:
                updates.append(line.split(","))

        except ValueError:
            pass

    pprint(rules)

    print()
    pprint(updates)

    acc = 0
    idx_a = 0

    correct_orders = sum(
        map(lambda update: 1 if is_correct_order(update) else 0, updates)
    )

    print(f"Correct: {correct_orders}")

    for update in updates:
        print(f"{idx_a}/{len(updates)}")
        idx_a += 1
        if not is_correct_order(update):

            while not is_correct_order(update):
                update = fix_order(update)

            print(update)

            idx = floor(len(update) / 2)
            middle = int(update[idx])

            acc += middle

    print(acc)
