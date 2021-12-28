from math import log, ceil


minRange = 273025
maxRange = 767253


def hasRepeat(number):
    lastDigit = str(number)[:1]
    seqSize = 1
    repeat = False

    for digit in str(number)[1:]:
        if (digit == lastDigit):
            seqSize += 1
        else:
            if (seqSize == 2):
                repeat = True
            seqSize = 1

        lastDigit = digit

    return repeat or seqSize == 2


def alwaysIncreasing(number):
    lastDigit = None

    for digit in str(number):
        if (lastDigit is not None and lastDigit > digit):
            return False
        lastDigit = digit

    return True


def isValid(number):
    if (not ceil(log(number, 10)) == 6):
        #   print("NOT 6")
        return False

    if (not hasRepeat(number)):
        #   print("NOT REPEAT", number)
        return False

    if (not alwaysIncreasing(number)):
        #   print("NOT INCREASING", number)
        return False

    if (not (number >= minRange and maxRange >= number)):
        #   print("NOT RANGE")
        return False

    return True


def script():
    count = 0

    for n in range(minRange, maxRange + 1):
        if (isValid(n)):
            count += 1

    return count


print(script())
