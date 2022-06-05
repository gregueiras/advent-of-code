from probe import Probe
from math import inf

#str = "target area: x=20..30, y=-10..-5"
str = "target area: x=111..161, y=-154..-101"

minX = str.split("..")[0].split("=")[1]
maxX = str.split("..")[1].split(",")[0]

minY = str.split("..")[1].split("=")[1]
maxY = str.split("..")[2]

hitCount = 0

nIter = 80

acc = 0
minI = 0

while acc < int(minX):
    minI += 1
    acc += minI

print(f"MinI: {minI}")


for i in range(minI, int(maxX) + 1):  # edge cases: minimum/maximum X
    for j in range(int(minY), -int(minY)+nIter):
        probe = Probe(minX, maxX, minY, maxY, i, j)

        while not probe.hit() and not probe.out():
            probe.step()

        if not probe.hit():
            continue

        hitCount += 1

print(hitCount)
