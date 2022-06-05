class Probe:
    def __init__(self, minX, maxX, minY, maxY, vX, vY) -> None:
        self.x = 0
        self.y = 0

        self.minX = int(minX)
        self.maxX = int(maxX)
        
        self.minY = int(minY)
        self.maxY = int(maxY)

        self.vX = vX
        self.vY = vY

        self.steps = [(self.x, self.y)]


    def step(self):
        self.x += self.vX
        self.y += self.vY

        if self.vX > 0:
            self.vX -= 1
        elif self.vX < 0:
            self.vX += 1

        self.vY -= 1

        self.steps.append((self.x, self.y))


    def hit(self) -> bool:
        minX = min([self.minX, self.maxX])
        maxX = max([self.minX, self.maxX])

        isInX = minX <= self.x <= maxX

        minY = min([self.minY, self.maxY])
        maxY = max([self.minY, self.maxY])

        isInY = minY <= self.y <= maxY

        return isInX and isInY

    def out(self):
        minX = min([self.minX, self.maxX])
        maxX = max([self.minX, self.maxX])

        isInX = minX <= self.x <= maxX

        return len(self.steps) > 500

        #return self.vX == 0 and not isInX




     