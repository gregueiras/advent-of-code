import os
from track import Track

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

players = [int(l.split(": ")[1]) for l in lines]

dice = 0

track = Track(10, players)

while True:
    for playerIdx in range(len(players)):
        rolls = []
        for roll in range(3):
            rolls.append((dice % 100) + 1)
            dice += 1

        track.move(playerIdx, rolls)
        if track.hasWon():
            print(dice * track.get2nd())
            exit(0)


    


