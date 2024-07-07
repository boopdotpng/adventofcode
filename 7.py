def getcounts(hand): return len(set(hand)), sorted([hand.count(c) for c in set(hand)], reverse=True)

def getType(hand):
  l, items = getcounts(hand)
  match l, *items:
    case 1, *_: t = 7 
    case 2, 4, *_: t = 6
    case 2, 3, *_: t = 5
    case 3, 3, *_: t = 4
    case 3, 2, 2, *_: t = 3
    case 4, 2, *_: t = 2
    case 5, *_: t = 1
  return t

# list of all possible hands with jokers replaced
def replacements(hand):
  if hand == "":
    return [""]
  return [
    x + y
    for x in ("23456789TQKA" if hand[0] == 'J' else hand[0])
    for y in replacements(hand[1:])
  ]

def process_line(line):
  line = line.strip().split(" ")
  hand, bid, t = line[0], int(line[1]), getType(line[0]) 

  if "J" in hand: 
    possibilities = replacements(hand)
    t = max(map(getType, possibilities))
  else:
    t = getType(hand)

  return hand, bid, t

def sortfn(a, b):
  # part 1 cards
  # cards = ['A', 'K', 'Q', 'J', 'T'] + [str(i) for i in range(9,1,-1)]
  # part 2 cards (joker as least valuable card)
  cards = ['A', 'K', 'Q', 'T'] + [str(i) for i in range(9,1,-1)] +  ['J']
  for ia, ib in zip(a,b):
    if ia == ib:
      continue
    # hand A is better, no need to switch
    elif cards.index(ia) < cards.index(ib):
      return False
    else:
      return True

def bubblesort(lines):
  for i in range(len(lines)):
    for j in range(0, len(lines)-i-1):
      a, _, at = lines[j]
      b, _, bt = lines[j+1]
      if at < bt:
        lines[j], lines[j+1] = lines[j+1], lines[j]
      elif at == bt and sortfn(a, b):
        lines[j], lines[j+1] = lines[j+1], lines[j]
  return lines

lines = bubblesort([
  process_line(line)
  for line in open("input.txt").readlines()
])
total = sum(
  [(i+1)*bid for i, (_, bid, _) in enumerate(reversed(lines))]
)
print(total)