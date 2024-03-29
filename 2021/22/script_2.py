import os
from aux import Reactor
from math import inf
from collections import Counter

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

reactor = Reactor(limit=inf)

cubes = Counter()
for line in lines:
    ins = reactor.read(line)
    update = Counter()
    nsgn = ins["value"] or -1
    nx0, nx1 = ins["x"]
    ny0, ny1 = ins["y"]
    nz0, nz1 = ins["z"]
    for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cubes.items():
        ix0 = max(nx0, ex0)
        ix1 = min(nx1, ex1)
        iy0 = max(ny0, ey0)
        iy1 = min(ny1, ey1)
        iz0 = max(nz0, ez0)
        iz1 = min(nz1, ez1)
        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn
    if nsgn > 0:
        update[(nx0, nx1, ny0, ny1, nz0, nz1)] += nsgn
    cubes.update(update)

print(sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn for (x0, x1, y0, y1, z0, z1), sgn in cubes.items()))
    
    
