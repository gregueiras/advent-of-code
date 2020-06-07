import numpy as np

WIDTH = 25
HEIGHT = 6

layers = np.full(shape=(HEIGHT, WIDTH), fill_value=-1)


def read_in_chunks(file_object, chunk_size=WIDTH*HEIGHT):
    """Lazy function (generator) to read a file piece by piece."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def process_data(layer):
    global layers

    idx = 0

    for digit in str(layer):
        if (digit == '2'):
            idx += 1
            continue

        if (layers.item(idx) == -1):
            np.put(layers, idx, int(digit))

        idx += 1


with open('./input.txt') as f:
    for piece in read_in_chunks(f):
        process_data(piece)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


for j in range(HEIGHT):
    for i in range(WIDTH):
        item = layers.item((j, i))

        if (item == 1):
            print(f"{bcolors.OKBLUE}O{bcolors.ENDC}", end="")
        elif (item == 0):
            print(f"{bcolors.FAIL}O{bcolors.ENDC}", end="")

    print(" ")
