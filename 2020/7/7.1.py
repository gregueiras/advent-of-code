import numpy as np
from numpy import loadtxt
import itertools


origNumbers = loadtxt("./input.txt", delimiter=",", unpack=False, dtype=int)
numbers = None


def readOpC(opC):
    numbers = []

    for i in str(opC):
        numbers.append(int(i))

    while len(numbers) < 5:
        numbers.insert(0, 0)

    numbers[3] = 10 * numbers[3] + numbers[4]
    del numbers[4]

    return numbers


def multiply(iterator, mode1, mode2):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    if (mode2):
        input2 = numbers[iterator + 2]
    else:
        input2 = numbers[numbers[iterator + 2]]

    numbers[numbers[iterator + 3]] = input1 * input2


def add(iterator, mode1, mode2):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    if (mode2):
        input2 = numbers[iterator + 2]
    else:
        input2 = numbers[numbers[iterator + 2]]

    numbers[numbers[iterator + 3]] = input1 + input2


def processInput(iterator, value):
    input1 = value

    numbers[numbers[iterator + 1]] = input1


def output(iterator, mode1):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    return input1


def jit(iterator, mode1, mode2):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    if (mode2):
        input2 = numbers[iterator + 2]
    else:
        input2 = numbers[numbers[iterator + 2]]

    if (input1 != 0):
        return input2
    else:
        return iterator + 3


def jif(iterator, mode1, mode2):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    if (mode2):
        input2 = numbers[iterator + 2]
    else:
        input2 = numbers[numbers[iterator + 2]]

    if (input1 == 0):
        return input2
    else:
        return iterator + 3


def lt(iterator, mode1, mode2):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    if (mode2):
        input2 = numbers[iterator + 2]
    else:
        input2 = numbers[numbers[iterator + 2]]

    numbers[numbers[iterator + 3]]

    if (input1 < input2):
        numbers[numbers[iterator + 3]] = 1
    else:
        numbers[numbers[iterator + 3]] = 0


def eq(iterator, mode1, mode2):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    if (mode2):
        input2 = numbers[iterator + 2]
    else:
        input2 = numbers[numbers[iterator + 2]]

    if (input1 == input2):
        numbers[numbers[iterator + 3]] = 1
    else:
        numbers[numbers[iterator + 3]] = 0


def iter(phase, prevOutput):
    print("A: ", prevOutput)
    iterator = 0
    input_idx = 0

    while iterator < numbers.size:
        _, mode2, mode1, opC = readOpC(numbers[iterator])

        if (opC == 1):
            add(iterator, mode1, mode2)
            iterator += 4
            continue

        if (opC == 2):
            multiply(iterator, mode1, mode2)
            iterator += 4
            continue

        if (opC == 3):
            processInput(iterator, phase if input_idx == 0 else prevOutput)
            input_idx += 1
            iterator += 2
            continue

        if (opC == 4):
            return output(iterator, mode1)

        if (opC == 5):
            iterator = jit(iterator, mode1, mode2)
            continue

        if (opC == 6):
            iterator = jif(iterator, mode1, mode2)
            continue

        if (opC == 7):
            lt(iterator, mode1, mode2)
            iterator += 4
            continue

        if (opC == 8):
            eq(iterator, mode1, mode2)
            iterator += 4
            continue

        if (opC == 99):
            print("HALT")
            return

    return numbers[0]


def script():
    global numbers

    maxValue = 0

    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))

    outputValue = 0
    for combination in permutations:
        for phase in combination:
            numbers = np.copy(origNumbers)
            outputValue = iter(phase, outputValue)

        if (outputValue > maxValue):
            maxValue = outputValue

        outputValue = 0

    print(maxValue)


script()
