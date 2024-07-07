from collections import deque
from dataclasses import dataclass

@dataclass 
class Card:
  winning: set 
  have: set 
  id: int
  def common(self) -> int:
    return len(self.winning & self.have)
  def score(self) -> int:
    return 2 ** (self.common() - 1) if self.common() != 0 else 0

def process_line(line):
  line = line.strip()
  ide = int(line[4:line.find(":")])-1
  line = line[line.find(":")+2:]
  line = line.split('|')  

  winning = line[0].split(' ')
  have = line[1].split(' ')

  w = set(winning)
  w.remove('')
  h = set(have)
  h.remove('')
  return Card(w, h, ide)

lines = [process_line(line) for line in open("input.txt", 'r').readlines()]

# part 1
# res = sum(card.score() for card in lines)
# print(res)

# part 2 
queue = deque([card for card in lines])
l = len(lines)
s = 0
while queue:
  card = queue.pop() 
  s += 1 
  stop = min(card.id + card.common(), l)
  queue.extendleft(lines[card.id+1:stop+1])
print(s)