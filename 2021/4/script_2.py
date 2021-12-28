import os
from typing import List
from board import Board

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)


numbers = lines[0].split(",")

acc = []
boards: List[Board] = []

for line in lines[2:]:
    if (line == ""):
        board = Board(acc)
        
        boards.append(board)
        acc = []
    else:
        temp = line.split(" ")
        temp = list(filter(None, temp))
        acc.append(temp)

board = Board(acc)

boards.append(board)

lastWin = None
for number in numbers:
    for board in boards:
        hasWin = board.play(number)
        
        if hasWin:
            lastWin = board.calcScore()

print(lastWin)

