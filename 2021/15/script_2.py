from pathlib import Path
from math import inf
from heapdict import heapdict

path = Path(__file__).parent / "./input.txt"

points = {}


def print_board(maxX, maxY):
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            print(points[(x, y)], end="")

        print("")


y = 0
with open(path) as fp:
    Lines = fp.readlines()
    dimY = len(Lines)
    for line in Lines:
        x = 0
        line = line.strip()

        dimX = len(line)

        for r in list(line):
            for i in range(5):
                for j in range(5):
                    newVal = int(r) + i + j
                    newVal += 1 if newVal >= 10 else 0

                    newX = x + i * dimX
                    newY = y + j * dimY

                    points[(newX, newY)] = (newVal) % 10
            x += 1

        y += 1


def dijkstra(start, end):
    Q = heapdict()
    dist = {}
    prev = {}

    dist[start] = 0

    for vertex in points.keys():
        if vertex != start:
            dist[vertex] = 1e8
            prev[vertex] = None

        Q[vertex] = dist[vertex]

    while len(Q.keys()) != 0:
        (u, _) = Q.popitem()

        if u == end:
            S = []
            acc = 0

            if prev[u] is not None or u == start:
                while u is not None:
                    S.insert(0, u)
                    acc += points[u]
                    try:
                        u = prev[u]
                    except KeyError:
                        u = None

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

            alt = dist[u] + points[v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                Q[v] = alt

    return dist, prev


maxX, maxY = [max(coords[i] for coords in points.keys()) for i in range(2)]

#print_board(maxX, maxY)
start = (0, 0)
end = (maxX, maxY)

print(f"{start} -> {end}")

S, acc = dijkstra(start, end)

# print(S)
print(acc)
