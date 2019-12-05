from math import inf


def calcNewPos(direction, value, x, y):
    incX = 0
    incY = 0

    if (direction == "R"):
        incX = 1
    if (direction == "U"):
        incY = 1
    if (direction == "L"):
        incX = -1
    if (direction == "D"):
        incY = -1

    return [x + incX, y + incY]


def script():
    board = {}
    filepath = 'input.txt'
    with open(filepath) as fp:
        line = fp.readline()
        index = 0

        while line:
            instructions = line.split(",")
            x = 0
            y = 0
            step = 0
            minDistance = inf

            for instruction in instructions:
                direction = instruction[:1]
                value = int(instruction[1:])

                for v in range(1, value + 1):
                    newX, newY = calcNewPos(direction, v, x, y)
                    x = newX
                    y = newY
                    step += 1

                    if (index == 0):
                        if (newX not in board):
                            board[newX] = []

                        oldX = board[newX]
                        oldX.extend([(newY, step)])

                        board[newX] = oldX
                    elif (index == 1):
                        if (newX in board):
                            column = dict(board[newX])
                            if (newY in column):
                                secondStep = column[newY]
                                newDistance = step + secondStep

                                if (newDistance < minDistance):
                                    minDistance = newDistance
            index += 1
            line = fp.readline()

        return minDistance


print(script())
