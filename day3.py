# lines = [line.strip() for line in open("input.txt", 'r').readlines()]
# rows = len(lines)
# cols = len(lines[0])
# s = 0 

# # false when symbol does not touch
# def testChar(r,c):
#   # left, right, up, down, 4 corners
#   positions = [
#     (r+1,c) if r+1 < rows else "",
#     (r-1,c) if r-1 > 0 else "",
#     (r, c+1) if c+1 < cols else "",
#     (r, c-1) if c-1 > 0 else "",
#     (r+1,c+1) if r+1 < rows and c+1 < cols else "", 
#     (r+1,c-1) if r+1 < rows and c-1 > 0 else "", 
#     (r-1,c-1) if r-1 > 0 and c-1 > 0 else "", 
#     (r-1,c+1) if r-1 > 0 and c+1 < cols else "", 
#   ]
#   positions = [pos for pos in positions if pos != ""]

#   return any([not lines[r][c].isdigit() and lines[r][c] != '.' for r,c in positions])

# for r, row in enumerate(lines):
#   buffer = ""
#   tests = []
#   for i, c in enumerate(row):
#     if c.isdigit():
#       buffer += c
#       tests.append(testChar(r,i))
#     elif not c.isdigit() or c == '.':
#       if any(tests) and len(buffer) > 0:
#         print(buffer)
#         s += int(buffer)
#       tests = []
#       buffer = ""
#   if any(tests) and len(buffer) > 0:
#     print(buffer)
#     s += int(buffer)

# print(s)

# part two 
lines = [line.strip() for line in open("input.txt").readlines()]
s = 0
def validPositions(r, c):
    oob = lambda r, c: (r >= 0 and r < len(lines)) and (c >= 0 and c < len(lines[0])) and lines[r][c].isdigit()
    positions = [
        (r-1, c-1), (r-1, c), (r-1, c+1),
        (r, c-1),             (r, c+1),
        (r+1, c-1), (r+1, c), (r+1, c+1)
    ]
    return [pos for pos in positions if oob(*pos)]

def findDigit(r,c):
  left = ""
  right = ""
  ptr = c
  while ptr < len(lines[0]) and lines[r][ptr].isdigit() :
      right += lines[r][ptr]      
      ptr += 1
  ptr = c - 1
  while ptr > -1 and lines[r][ptr].isdigit():
      left += lines[r][ptr]      
      ptr -= 1
  return int(left[::-1] + right)

for r, row in enumerate(lines):
  buffer = ""
  for i, c in enumerate(row):
    if c == "*":
      valid = validPositions(r,i)
      nums = set(findDigit(*pos) for pos in valid)
      if len(nums) == 2:
        s += list(nums)[0] * list(nums)[1]

print(s)