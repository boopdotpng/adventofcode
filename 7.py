def getcounts(hand):
  from collections import defaultdict
  counts = defaultdict(int)
  for c in hand: 
    counts[c] += 1 
  
  return len(counts.keys()), [x for _, x in sorted(list(counts.items()), key=lambda x: x[1], reverse=True)]

def process_line(line):
  line = line.strip().split(" ")
  hand, bid, t = line[0], int(line[1]), 0
  l, items = getcounts(hand)
  if l == 1:
    t = 7
  elif l == 2 and items[0] == 4:
    t = 6
  elif l == 2 and items[0] == 3:
    t = 5
  elif l == 3 and items[0] == 3:
    t = 4
  elif l == 3 and items[0] == 2 and items[1] == 2:
    t = 3
  elif l == 4 and items[0] == 2:
    t = 2
  elif l == 5:
    t = 1
  return hand, bid, t

def sortfn(a, b):
  cards = ['A', 'K', 'Q', 'J', 'T'] + [str(i) for i in range(9,1,-1)]
  for ia, ib in zip(a,b):
    if ia == ib:
      continue
    # hand A is better, no need to switch
    elif cards.index(ia) < cards.index(ib):
      return False
    else:
      return True

def bubblesort():
  for i in range(len(lines)):
    for j in range(0, len(lines)-i-1):
      a, _, at = lines[j]
      b, _, bt = lines[j+1]
      if at == bt and sortfn(a, b):
          lines[j], lines[j+1] = lines[j+1], lines[j]

lines = [
  process_line(line)
  for line in open("input.txt").readlines()
]
lines.sort(key=lambda x: x[2], reverse=True)
bubblesort()
for i in [ ','.join([hand, str(bid), str(t)]) for hand, bid, t in lines[::-1]]:
  print(i)
total = sum(
  [(i+1)*bid for i, (_, bid, _) in enumerate(reversed(lines))]
)
print(total)