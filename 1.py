# lines = [line.strip() for line in open("input.txt", 'r').readlines() ]
# s = 0

# for line in lines:
#   buffer = []
#   for c in line:
#     if not c.isalpha():
#       buffer.append(int(c))
  
#   s += buffer[0]*10 + buffer[-1] if len(buffer) > 1 else buffer[0]*10 + buffer[0]

# print(s)

#! part two
lines = [line.strip() for line in open("input.txt", 'r').readlines()]
valid = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
s = 0
for line in lines:
  flag = False
  for c in range(1, len(line)):
    l = line[:c]
    if l[-1].isdigit():
      i = int(l[-1]) * 10
      print("start", i//10)
      s+=i
      break
    if len(l) >= 3:
      for v in valid: 
        if v in l:
          i = (valid.index(v) + 1) * 10
          print("start", i//10)
          s += i
          flag = True
          break
    if flag:
      break
    
  flag = False
  for c in range(1, len(line)):
    l = line[len(line)-c: len(line)]
    if l[0].isdigit():
      i = int(l[0]) 
      print(i)
      s+=i
      break
    if len(l) >= 3:
      for v in valid: 
        if v in l:
          i = valid.index(v) + 1
          print(i)
          s += i
          flag = True
          break
    if flag:
      break
print(s)