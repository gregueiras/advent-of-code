import os

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


with open(PATH) as file_in:
    city = []

    for line in file_in:
        try:
            line = line.strip()
            city.append(list(line))
        except ValueError:
            pass

    for line in city:
        print("".join(line))

    print("---")

    acc = 0

    antennas = {}

    for y in range(len(city)):
        for x in range(len(city[0])):
            pos = city[y][x]
            if pos != ".":
                if pos not in antennas:
                    antennas[pos] = []

                antennas[pos].append((x, y))

    antinodes = set()

    for antenna, coords in antennas.items():
        for idx_0 in range(len(coords)):
            coord_0 = coords[idx_0]
            for idx_1 in range(idx_0 + 1, len(coords)):
                coord_1 = coords[idx_1]

                diff_x = abs(coord_0[0] - coord_1[0])
                diff_y = abs(coord_0[1] - coord_1[1])

                if (coord_0[0] < coord_1[0]):
                    new_cords_0 = (coord_0[0] - diff_x, coord_0[1] - diff_y)
                    new_cords_1 = (coord_1[0] + diff_x, coord_1[1] + diff_y)
                else:
                    new_cords_0 = (coord_0[0] + diff_x, coord_0[1] - diff_y)
                    new_cords_1 = (coord_1[0] - diff_x, coord_1[1] + diff_y)


                changed = False

                if 0 <= new_cords_0[0] < len(city[0]) and 0 <= new_cords_0[1] < len(city):
                    new_pos_0 = city[new_cords_0[1]][new_cords_0[0]]
                    antinodes.add(new_cords_0)
                    if new_pos_0 == ".":
                        city[new_cords_0[1]][new_cords_0[0]] = "#"
                        changed = True
                
                if 0 <= new_cords_1[0] < len(city[0]) and 0 <= new_cords_1[1] < len(city):
                    new_pos_1 = city[new_cords_1[1]][new_cords_1[0]]
                    antinodes.add(new_cords_1)
                    if new_pos_1 == ".":
                        city[new_cords_1[1]][new_cords_1[0]] = "#"
                        changed = True

                if changed:
                    for line in city:
                        print("".join(line))

                    print("---")



    for line in city:
        print("".join(line))

    print("---")
    print(len(antinodes))