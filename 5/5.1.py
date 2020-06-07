from numpy import loadtxt

numbers = loadtxt("./input.txt", delimiter=",", unpack=False, dtype=int)


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


def processInput(iterator):
    input1 = input("Input: ")

    numbers[numbers[iterator + 1]] = input1


def output(iterator, mode1):
    if (mode1):
        input1 = numbers[iterator + 1]
    else:
        input1 = numbers[numbers[iterator + 1]]

    print(input1)


def script():
    iterator = 0

    while iterator < numbers.size:
        mode3, mode2, mode1, opC = readOpC(numbers[iterator])

        if (opC == 1):
            add(iterator, mode1, mode2)
            iterator += 4
            continue

        if (opC == 2):
            multiply(iterator, mode1, mode2)
            iterator += 4
            continue

        if (opC == 3):
            processInput(iterator)
            iterator += 2
            continue

        if (opC == 4):
            output(iterator, mode1)
            iterator += 2
            continue

        if (opC == 99):
            print("HALT")
            return

    return numbers[0]


print(script())
