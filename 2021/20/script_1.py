import os
import sys
import math

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
padding = 600


with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

alg = lines[0]
img = lines[2:]


class Img:
    def __init__(self, input, alg) -> None:
        self.alg = alg
        
        self.row = len(input)
        self.col = len(input[0])

        self.out = [['.' for _ in range(padding)] for _ in range(padding)]
        for i in range(self.row):
            for a in range(self.col):
                self.out[i + padding // 2][a + padding // 2] = input[i][a]
        #self.input = self.out.copy()

        self.input = [row[:] for row in self.out]

    def getSurrounding(self, i, a):
        num = ''
        for xi in range(-1, 2):
            for xa in range(-1, 2):
                newi = xi + i
                newa = xa + a

                num += '1' if self.input[newi][newa] == '#' else '0'

        return int(num, 2)

    def output(self, n):
        minIdx = 1
        maxIdx = padding - 1

        for _ in range(n):
            count = 0
            for i in range(minIdx, maxIdx):
                for a in range(minIdx, maxIdx):
                    idx = self.getSurrounding(i, a)
                    res = self.alg[idx]

                    self.out[i][a] = res

            minIdx += 1
            maxIdx -= 1

            count = 0
            for i in range(minIdx, maxIdx):
                for a in range(minIdx, maxIdx):
                    if self.out[i][a] == '#':
                        count += 1
            print(count)

            self.input = [row[:] for row in self.out]



res = Img(img, alg)
res.output(50)
