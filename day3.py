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
def find_adjacent_numbers(r, c, numbers):
    adjacent = []
    for num, (row, length, col) in numbers.items():
        if (r-1 <= row <= r+1) and (col-1 <= c <= col+length):
            adjacent.append(num)
    return adjacent

lines = [line.strip() for line in open("input.txt", 'r').readlines()]
rows, cols = len(lines), len(lines[0])

numbers = {}
symbols = []

for r, row in enumerate(lines):
    buffer = ""
    for c, char in enumerate(row):
        if char.isdigit():
            buffer += char
        else:
            if buffer:
                numbers[int(buffer)] = (r, len(buffer), c - len(buffer))
                buffer = ""
            if char == '*':
                symbols.append((r, c))
    if buffer:
        numbers[int(buffer)] = (r, len(buffer), cols - len(buffer))

total_gear_ratio = 0

for r, c in symbols:
    adjacent_nums = find_adjacent_numbers(r, c, numbers)
    if len(adjacent_nums) == 2:
        gear_ratio = adjacent_nums[0] * adjacent_nums[1]
        total_gear_ratio += gear_ratio

print(total_gear_ratio)