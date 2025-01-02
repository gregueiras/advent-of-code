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

                new_cords = []
                new_cords.append(coord_0)
                new_cords.append(coord_1)

                if (coord_0[0] < coord_1[0]):
                    new_x = coord_0[0] - diff_x
                    new_y = coord_0[1] - diff_y

                    while(new_x >= 0 and new_y >= 0):
                        new_cords.append((new_x, new_y))
                        new_x -= diff_x
                        new_y -= diff_y

                    new_x = coord_1[0] + diff_x
                    new_y = coord_1[1] + diff_y

                    while(new_x < len(city[0]) and new_y < len(city)):
                        new_cords.append((new_x, new_y))
                        new_x += diff_x
                        new_y += diff_y

                else:
                    new_x = coord_0[0] + diff_x
                    new_y = coord_0[1] - diff_y

                    while(new_x < len(city[0]) and new_y >= 0):
                        new_cords.append((new_x, new_y))
                        new_x += diff_x
                        new_y -= diff_y

                    new_x = coord_1[0] - diff_x
                    new_y = coord_1[1] + diff_y

                    while(new_x >= 0 and new_y < len(city)):
                        new_cords.append((new_x, new_y))
                        new_x -= diff_x
                        new_y += diff_y

                for new_cord in new_cords:
                    changed = False

                    if 0 <= new_cord[0] < len(city[0]) and 0 <= new_cord[1] < len(city):
                        new_pos_0 = city[new_cord[1]][new_cord[0]]
                        antinodes.add(new_cord)
                        if new_pos_0 == ".":
                            city[new_cord[1]][new_cord[0]] = "#"
                            changed = True

                if changed:
                    for line in city:
                        print("".join(line))

                    print("---")



    for line in city:
        print("".join(line))

    print("---")
    print(len(antinodes))