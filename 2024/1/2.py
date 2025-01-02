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

    frequencies = {}
    for right in list_right:
        if right in frequencies:
            frequencies[right] += 1
        else:
            frequencies[right] = 1

    acc = 0
    for left in list_left:
        if left in frequencies:
            acc += frequencies[left] * left

    print(acc)

