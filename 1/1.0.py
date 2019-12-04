from math import floor


def calc(mass):
    return floor(mass / 3) - 2


def script():
    filepath = 'input.txt'
    with open(filepath) as fp:
        line = fp.readline()
        total = 0

        while line:
            mass = int(line)
            fuel = calc(mass)
            total += int(fuel)
            line = fp.readline()

        return total


print(script())
