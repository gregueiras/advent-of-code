import os

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

orig_fishes = lines[0].split(",")
orig_fishes = list(map(lambda val: int(val), orig_fishes))

fishes = [0 for _ in range(0, 9)]
for fish in orig_fishes:
    fishes[fish] += 1


target = 256

print(f"Initial state: {fishes}")
for day in range(1, target + 1):
    new_fishes = [0 for _ in range(0, 9)]

    for idx in range(len(fishes) - 1, -1, -1):
        if idx == 0:
            new_fishes[len(new_fishes) - 1] = fishes[idx]
            new_fishes[6] += fishes[idx]
        else:
            new_fishes[idx - 1] = fishes[idx]


    fishes = new_fishes
    #print(f"After  {str(day).ljust(2)} day: {fishes}")
    print(f"After {str(day).ljust(2)} day: {sum(fishes)} fishes\r", end="" if day != target else "\n")


