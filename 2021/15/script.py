from pathlib import Path
from math import inf

path = Path(__file__).parent / "./test_input.txt"

points = {}


def print_board(maxX, maxY):
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            print(points[(x, y)], end="")

        print("")


y = 0
with open(path) as fp:
    Lines = fp.readlines()
    for line in Lines:
        x = 0
        line = line.strip()

        for r in list(line):
            points[(x, y)] = int(r)
            x += 1

        y += 1


def findInSet(set, dist):
    minVal = inf
    minKey = None

    for key in set.keys():
        val = dist[key]
        if val < minVal:
            minVal = val
            minKey = key

    return minKey


def dijkstra(start, end):
    Q = points.copy()
    dist = {}
    prev = {}

    for vertex in Q.keys():
        dist[vertex] = inf
        prev[vertex] = None

    dist[start] = 0

    while len(Q.keys()) != 0:
        u = findInSet(Q, dist)

        Q.pop(u)

        if u == end:
            S = []
            acc = 0

            if prev[u] is not None or u == start:
                while u is not None:
                    S.insert(0, u)
                    acc += points[u]
                    u = prev[u]

                acc -= points[start]

            return S, acc

        x, y = u
        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]

        for v in neighbors:
            if not v in Q.keys():
                continue

            alt = dist[u] + Q[v]

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


maxX, maxY = [max(coords[i] for coords in points.keys()) for i in range(2)]

#print_board(maxX, maxY)
start = (0, 0)
end = (maxX, maxY)

S, acc = dijkstra(start, end)

# print(S)
print(acc)
