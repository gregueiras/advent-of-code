from aux import Packet
import os

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)


def sum_versions(packet: Packet):
    if len(packet.packets) == 0:
        return packet.version

    acc = 0
    for p in packet.packets:
        acc += sum_versions(p)

    return acc + packet.version


def convert_str(hexdata: str):
    scale = 16  # equals to hexadecimal
    temp = bin(int(hexdata, scale))[2:]

    padding = 4 - len(temp) % 4 + len(temp) if len(temp) % 4 != 0 else 0

    converted = temp.zfill(padding)

    return converted


my_hexdata = lines[0]

pkt = Packet(convert_str(my_hexdata))

print(pkt.value)

