from math import log, ceil


minRange = 273025
maxRange = 767253


def hasRepeat(number):
    lastDigit = None

    for digit in str(number):
        if (lastDigit is not None and digit == lastDigit):
            return True
        lastDigit = digit

    return False


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

    for n in range(minRange + 1, maxRange):
        if (isValid(n)):
            count += 1

    return count


print(script())
