import os
PATH = os.path.join(os.path.dirname(__file__), "input.txt")

class Mem():
    def __init__(b, pos, len): b.pos = pos; b.len = len
    def val(b): return (2*b.pos + b.len-1) * b.len // 2

with open(PATH) as file_in:
  line = file_in.readline().strip()

  pos, mem = 0, []
  for len in map(int, line):
      mem += [Mem(pos, len)]
      pos += len

  for used in mem[::-2]:
      for free in mem[1::2]:
          if (free.pos <= used.pos
          and free.len >= used.len):
              used.pos  = free.pos
              free.pos += used.len
              free.len -= used.len

  print(sum(id*m.val() for id, m in enumerate(mem[::2])))