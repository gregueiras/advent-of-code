from numpy import loadtxt


numbers = loadtxt("input.txt", delimiter=",", unpack=False, dtype=int)


def multiply(iterator):
    input1 = numbers[numbers[iterator + 1]]
    input2 = numbers[numbers[iterator + 2]]
    numbers[numbers[iterator + 3]] = input1 * input2


def add(iterator):
    input1 = numbers[numbers[iterator + 1]]
    input2 = numbers[numbers[iterator + 2]]
    numbers[numbers[iterator + 3]] = input1 + input2


def script():
    iterator = 0
    numbers[1] = 12
    numbers[2] = 2

    while iterator < numbers.size:
        opC = numbers[iterator]

        if (opC == 1):
            add(iterator)
        if (opC == 2):
            multiply(iterator)
        if (opC == 99):
            print("HALT")

        iterator += 4

    return numbers[0]


print(script())
