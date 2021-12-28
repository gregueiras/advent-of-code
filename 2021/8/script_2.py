import os
from aux import Display
from typing import List

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)


inputs: List[List[str]] = []
outputs: List[List[str]] = []
for line in lines:
    temp = line.split(" | ")
    
    inp = temp[0].split(" ")
    out = temp[1].split(" ")

    inputs.append(inp)
    outputs.append(out)


acc = 0
for inp, out in zip(inputs, outputs):
    disp = Display()

    while not disp.finished():
        for i in inp:
            disp.guess(i)

    acc += disp.calcOutput(out)

print(acc)