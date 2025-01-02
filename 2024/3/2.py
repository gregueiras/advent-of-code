import os
import math
import pprint
import re

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

with open(PATH) as file_in:
    instructions = ""

    for line in file_in:
        try:
            instructions += line
        except ValueError:
            pass

    acc = 0

    regex = r"mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)"

    
    matches = re.finditer(regex, instructions, re.MULTILINE)

    do = True
    for matchNum, match in enumerate(matches, start=1):
        groups = tuple([i for i in match.groups() if i is not None])

        if len(groups) == 1:
            instruction = groups[0]
            if (instruction == "do"):
                do = True
                print("DO")
            elif (instruction == "don\'t"):
                do = False
                print("DONT")
        elif do:
            groups = list(map(int, groups))
            print(groups)
            acc += groups[0] * groups[1]

    print(acc)


            
