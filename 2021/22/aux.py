class Reactor:
    def __init__(self, limit=50) -> None:
        self.cubes = {}
        self.limit = limit

    def read(self, inst):
        state = inst.split(" ")[0] == "on"

        xMin = int(inst.split("=")[1].split("..")[0])
        xMax = int(inst.split("=")[1].split("..")[1].split(",")[0])

        yMin = int(inst.split("=")[2].split("..")[0])
        yMax = int(inst.split("=")[2].split("..")[1].split(",")[0])
        
        zMin = int(inst.split("=")[3].split("..")[0])
        zMax = int(inst.split("=")[3].split("..")[1].split(",")[0])

        return {
            "value": state,
            "x": (xMin, xMax),
            "y": (yMin, yMax),
            "z": (zMin, zMax),
        }


    def instruction(self, inst):
        state = inst.split(" ")[0] == "on"

        xMin = int(inst.split("=")[1].split("..")[0])
        xMax = int(inst.split("=")[1].split("..")[1].split(",")[0])

        yMin = int(inst.split("=")[2].split("..")[0])
        yMax = int(inst.split("=")[2].split("..")[1].split(",")[0])
        
        zMin = int(inst.split("=")[3].split("..")[0])
        zMax = int(inst.split("=")[3].split("..")[1].split(",")[0])

        if (xMax < -self.limit or xMin > self.limit) or (yMax < -self.limit or yMin > self.limit) or (zMax < -self.limit or zMin > self.limit):
            return
        
        xMax = sorted((-self.limit, xMax, self.limit))[1]
        xMin = sorted((-self.limit, xMin, self.limit))[1]
        yMin = sorted((-self.limit, yMin, self.limit))[1]
        yMax = sorted((-self.limit, yMax, self.limit))[1]
        zMin = sorted((-self.limit, zMin, self.limit))[1]
        zMax = sorted((-self.limit, zMax, self.limit))[1]

        for x in range(xMin, xMax + 1):
            for y in range(yMin, yMax + 1):
                for z in range(zMin, zMax + 1):
                    key = f"{x},{y},{z}"
                    
                    if state:
                        self.cubes[key] = True
                    else:
                        if key in self.cubes:
                            self.cubes.pop(key)
