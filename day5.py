from dataclasses import dataclass

@dataclass
class Map:
  dest: int
  source: int
  l: int

@dataclass
class Group:
  maps: list
  def addMap(self, dest, source, l):
    self.maps.append(Map(dest, source, l))
  def map(self, input):
    for map in self.maps:
      if input >= map.source and input <= map.source+map.l:
        print(map.dest + (input - map.source))
        return map.dest + (input - map.source) 
    return input

def parse_input():
  lines = [line.strip() for line in open("input.txt").readlines() if line.strip() != ""]
  seeds = list(map(int,lines[0][lines[0].find(":")+1:].strip().split(' ')))
  groups = []

  buffer = []
  for line in lines[2:]:
    buffer.append(line)
    if ":" in line:
      g = Group(maps=[])
      for m in buffer[:-1]:
        dest, source, l = m.split(' ')
        g.addMap(int(dest), int(source), int(l))
      groups.append(g)
      buffer = []
  
  return seeds, groups

seeds, groups = parse_input()
res = []
for seed in [79]:
  for g in groups:
    seed = g.map(seed)
  res.append(seed)

print(min(res))