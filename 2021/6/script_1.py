import os

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

fishes = lines[0].split(",")
fishes = list(map(lambda val: int(val), fishes))

target = 80

print(f"Initial state: {fishes}")
for day in range(1, target + 1):
    temp = []
    new_fishes = []

    for fish in fishes:
        if fish == 0:
            temp.append(6)
            new_fishes.append(8)
        else:
            temp.append(fish - 1)

    temp.extend(new_fishes)
    fishes = temp

    #print(f"After  {str(day).ljust(2)} day: {fishes}")


print(len(fishes))
