WIDTH = 25
HEIGHT = 6

layers = []


def read_in_chunks(file_object, chunk_size=WIDTH*HEIGHT):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def process_data(layer):
    zeros = 0
    ones = 0
    twos = 0

    for digit in str(layer):
        if (digit == '0'):
            zeros += 1
            continue

        if (digit == '1'):
            ones += 1
            continue

        if (digit == '2'):
            twos += 1
            continue

    layers.append((zeros, ones, twos))


with open('./input.txt') as f:
    for piece in read_in_chunks(f):
        process_data(piece)


minLayer = min(layers)
ans = minLayer[1] * minLayer[2]

print(ans)
