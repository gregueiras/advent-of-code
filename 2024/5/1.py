from typing import List
import os
from pprint import pprint
from math import floor

PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def is_correct_order(update: List[str]) -> bool:
    for idx in range(len(update)):
        page = update[idx]

        if page in rules:
            afters = rules[page]
            prefix = update[:idx]
            suffix = update[idx:]

            for after in afters:
                if after in prefix:
                    return False

    return True


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

    for update in updates:
        if is_correct_order(update):
            idx = floor(len(update) / 2)
            middle = int(update[idx])

            acc += middle

    print(acc)
