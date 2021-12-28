import os
from typing import List
from aux import Board, Instruction

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)


instructions: List[Instruction] = []
for line in lines:
    inst = Instruction(line)
    if inst.isHorizontal() or inst.isVertical():
        instructions.append(inst)

board = Board(instructions)

for instruction in instructions:
    board.play(instruction)
"""     print(instruction)
    print(board)

    print("\n\n --- \n\n")
 """    

#print(board)
print(board.score(2))


