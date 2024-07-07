lines = [line.strip() for line in open("input.txt").readlines()]

seeds = lines[0][lines[0].find(":")+2:].split(' ')
seeds = list(map(int, seeds))
maps = []

def process_buffer(buffer):
  buffer = buffer[1:]
  m = []
  for group in buffer:
    if group == '': continue
    dest, source, range = group.split(' ')
    m.append(
      list(map(int, (dest, source, range)))
    )
  if len(m) > 0:
    maps.append(m) 

buffer = []
for line in lines[1:]:
  if ":" in line:
    # processs 
    process_buffer(buffer)
    buffer = []
    pass
  buffer.append(line)
process_buffer(buffer)

finals = []
# for seed in seeds:
#   for section in maps:
#     for dest, source, r in section:
#       if seed in range(source, source+r+1):
#         seed = dest + (seed - source)
#         break
#   finals.append(seed)

# print(min(finals))

# part two
for i in range(0, len(seeds)-1, 2):
  st, r = seeds[i:i+2]
  for seed in range(st, st+r):
    for section in maps:
      for dest, source, r in section:
        if seed in range(source, source+r+1):
          seed = dest + (seed - source)
          break
    finals.append(seed)
print(min(finals))