from math import prod
from typing import List

evalCounter = 0

class Packet:
    def __init__(self, converted) -> None:
        self.converted = converted
        self.version = int(converted[:3], 2)
        self.type = int(converted[3:6], 2)
        self.packets = []

        self.size = 0
        self.value = None

        if self.type == 4:
            self._parseValue()
        else:
            self._parseOperator()

        self.value = self._evaluate()


    def _evaluate(self):
        if self.value is not None:
            return self.value

        functions = {
            0: self._sum,
            1: self._prod,
            2: self._min,
            3: self._max,
            4: self._ret,
            5: self._gt,
            6: self._lt,
            7: self._eq,
        }

        return functions[self.type]()

    def _evaluateAll(self):
        return list(map(lambda p: p._evaluate(), self.packets))

    def _sum(self):
        return sum(self._evaluateAll())

    def _prod(self):
        return prod(self._evaluateAll())

    def _min(self):
        return min(self._evaluateAll())
    
    def _max(self):
        return max(self._evaluateAll())

    def _ret(self):
        return self.value

    def _gt(self):
        pckt0 = self.packets[0]
        pckt1 = self.packets[1]

        val = pckt0._evaluate() > pckt1._evaluate()

        return int(val)
    
    def _lt(self):
        pckt0 = self.packets[0]
        pckt1 = self.packets[1]

        val = pckt0._evaluate() < pckt1._evaluate()

        return int(val)

    def _eq(self):
        pckt0 = self.packets[0]
        pckt1 = self.packets[1]

        val = pckt0._evaluate() == pckt1._evaluate()

        return int(val)


    def _parseValue(self):
        idx = 6
        keepReading = True
        valueStr = ""
        while keepReading:
            keepReading = self.converted[idx] == "1"
            idx += 1

            valueStr += self.converted[idx:idx+4]
            idx += 4

        self.size = idx
        self.value = int(valueStr, 2)

    def _parseOperator(self):
        idx = 6
        lengthType = self.converted[idx]

        if lengthType == '0':
            idx += 1
            length = int(self.converted[idx: idx + 15], 2)
            idx += 15

            origIdx = idx
            packets = []
            remaining = length
            while idx < origIdx + length: #and int(self.converted[idx:idx + length]) != 0:
                newPacket = Packet(self.converted[idx: idx + remaining])
                packets.append(newPacket)
                idx += newPacket.size
                remaining -= newPacket.size

        elif lengthType == '1':
            idx += 1
            n = int(self.converted[idx: idx + 11], 2)
            idx += 11

            packets = []
            for i in range(n):
                newPacket = Packet(self.converted[idx:])
                packets.append(newPacket)
                idx += newPacket.size

        self.packets: List[Packet] = packets
        self.size += idx
