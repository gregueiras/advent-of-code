import os
import math
import pprint
import re

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

with open(PATH) as file_in:
    reports = []

    for line in file_in:
        try:
            reports.append(line)
        except ValueError:
            pass

    acc = 0

    regex = r"mul\((\d+),(\d+)\)"
    for report in reports:
        matches = re.finditer(regex, report, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            groups = list(map(int, match.groups()))
            acc += groups[0] * groups[1]

    print(acc)


            
