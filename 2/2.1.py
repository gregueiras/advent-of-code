from numpy import loadtxt


ogNumbers = loadtxt("input.txt", delimiter=",", unpack=False, dtype=int)
numbers = None


def multiply(iterator):
    global numbers

    input1 = numbers[numbers[iterator + 1]]
    input2 = numbers[numbers[iterator + 2]]
    numbers[numbers[iterator + 3]] = input1 * input2


def add(iterator):
    global numbers

    input1 = numbers[numbers[iterator + 1]]
    input2 = numbers[numbers[iterator + 2]]
    numbers[numbers[iterator + 3]] = input1 + input2


def script():
    global numbers

    iterator = 0
    instructionPointer = 0

    while iterator < len(numbers):
        opC = numbers[iterator]

        if (opC == 1):
            add(iterator)
            instructionPointer += 4
        elif (opC == 2):
            multiply(iterator)
            instructionPointer += 4
        elif (opC == 99):
            print("HALT")

        iterator += 4

    return numbers[0]
    # return instructionPointer


def findPair(desiredOutput):
    global numbers

    noun = 0
    verb = 0

    while noun <= 100:
        verb = 0
        while verb <= 100:
            numbers = list(ogNumbers)
            numbers[1] = noun
            numbers[2] = verb

            output = script()
            print(numbers[0])
            if (output == desiredOutput):
                return [noun, verb]
            else:
                print(f"NOT\t{noun}\t{verb}")

            verb += 1

        noun += 1

    return - 1


print(findPair(19690720))
