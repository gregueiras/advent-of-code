import functools as ft

with open('24/input.txt') as f:
	lines = f.read().splitlines()

blocks = []
cur_block = []

for line in lines:
    instr = line.split(" ")
    if instr[0] == 'inp':
        assert(instr[1] == "w")
        blocks.append(cur_block)
        cur_block = []
    else:
        cur_block.append(instr)


blocks.append(cur_block)
blocks = blocks[1:]

chars = 'wxyz'

def asm(idx, w, z):
    vals = [w, 0, 0, z]
    for instr in blocks[idx]:
        inst = instr[0]
        register = chars.index(instr[1])

        try:
            val = int(instr[2])
        except:
            val = vals[chars.index(instr[2])]

        if inst == 'add':
            vals[register] += val
        elif inst == 'mul':
            vals[register] *= val
        elif inst == 'div':
            vals[register] //= val
        elif inst == 'mod':
            vals[register] %= val
        else:
            assert(inst == 'eql')
            vals[register] = int(vals[register] == val)

    
    return vals[3]


path = []

@ft.lru_cache
def recur(idx, cur_z):
    global path
    if idx == len(blocks):
        if cur_z == 0:
            print(''.join([str(p) for p in path]))
            return True
        return False

    for w in range(9, 0, -1):
        path.append(w)
        if recur(idx + 1, asm(idx, w, cur_z)):
            return True
        print(f"\r{''.join([str(p) for p in path])}", end="")
        path = path[:-1]
    return False

recur(0, 0)