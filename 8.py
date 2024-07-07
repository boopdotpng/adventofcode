from collections import defaultdict
graph = defaultdict(list) 
def parse(line):
  line = line.strip().split("=")
  label = line[0][:-1]

  left, right = line[1].split(',')

  return label, left[2:], right[1:-1]

def buildNode(line):
  label, left, right = parse(line)
  graph[label].extend([left, right])

lines = open("input.txt").readlines()
ins = lines[0].strip()
for l in lines[2:]:
  buildNode(l)

# part one
# current = "AAA"
# i = 0
# steps = 0

# while current != "ZZZ":
#   if ins[i] == "L":
#     current = graph[current][0] 
#   else:
#     current = graph[current][1] 
#   i = (i+1) % len(ins)
#   steps += 1
# print(steps)

# part two
steps = 0
i = 0
starts = [key for key in graph.keys() if key.endswith('A')]
endings = []
exclude = []
while len(exclude) < len(starts):
  if ins[i] == 'L':
    for j, s in enumerate(starts):
      if j in exclude: continue
      starts[j] = graph[starts[j]][0] 
  else:
    for j, s in enumerate(starts):
      if j in exclude: continue
      starts[j] = graph[starts[j]][1] 

  i = (i+1) % len(ins)
  steps += 1
  for e, st in enumerate(starts):
    if st.endswith("Z") and e not in exclude:
      endings.append(steps)
      exclude.append(e)

import math 
print(math.lcm(*endings))