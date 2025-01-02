import os
import math
import pprint
from typing import List

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

def approach_0(reports, acc):
    for report in reports:
        last_level = report[0]
        order = None
        safe = True

        for level in report[1:]:
            if level == last_level:
                safe = False
                break

            if order is None:
                order = last_level < level
            else:
                if (order and last_level > level) or (order and last_level > level):
                    safe = False
                    break

            diff = math.fabs(level - last_level)
            if diff < 1 or diff > 3:
                safe = False
                break

            last_level = level

        if safe:
            acc += 1

def approach_1(report):
    diff = []

    for left, right in zip(report[0:-1], report[1:]):
        diff.append(left - right)

    same = 0 in diff
    bigger = max(diff) > 3 or min(diff) < -3

    is_negative = diff[0] < 0
    changed_order = False
    for d in diff:
        if is_negative and d > 0:
            changed_order = True
        elif not is_negative and d < 0:
            changed_order = True

    return (not same) and (not bigger) and (not changed_order)


with open(PATH) as file_in:
    reports: List[List[int]] = []

    for line in file_in:
        try:
            line = list(map(int, line.split()))
            reports.append(line)
        except ValueError:
            pass

    acc = 0

    for report in reports:
        if approach_1(report):
            acc += 1
        else:
            for idx in range(len(report)):
                if approach_1(report[0:idx] + report[idx+1:]):
                    acc += 1
                    break


    print(acc)



            
