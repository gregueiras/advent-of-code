import os
import math

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    list_left = []
    list_right = []

    for line in file_in:
        try:
            line = line.split()
            list_left.append(int(line[0]))
            list_right.append(int(line[1]))
        except ValueError:
            pass

    list_left = sorted(list_left)
    list_right = sorted(list_right)

    acc = 0

    diff = [math.fabs(left - right) for left, right in zip(list_left, list_right)]

    acc = sum(diff)
    print(acc)

