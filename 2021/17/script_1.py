from probe import Probe
from math import inf

#str = "target area: x=20..30, y=-10..-5"
str = "target area: x=111..161, y=-154..-101"

minX = str.split("..")[0].split("=")[1]
maxX = str.split("..")[1].split(",")[0]

minY = str.split("..")[1].split("=")[1]
maxY = str.split("..")[2]

myMaxY = -inf
maxV = None

nIter = 6000

for i in range(13, 16):
    for j in range(1, nIter):
        probe = Probe(minX, maxX, minY, maxY, i, j)

        while not probe.hit() and not probe.out():
            probe.step()

        #print(probe.steps)
        #print()

        if not probe.hit():
            continue

        thisMaxY = max(list(map(lambda step: step[1], probe.steps)))
        if thisMaxY > myMaxY:
            myMaxY = thisMaxY
            maxV = (i, j)


print(myMaxY)
print(maxV)