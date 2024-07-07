# times, distances = [55,82, 64, 90], [246, 1441, 1012, 1111]
times, distances = [7, 15, 30], [9,40,200]

def part1(t,d):
  count = 0
  for speed in range(1, t):
    dist = speed * (t - speed)
    if dist > d:
      count += 1
  return count

# total = [part1(t,d) for t,d in zip(times, distances)]
# p = 1 
# for t in total: p *= t
# print(p)

time, distance = 55826490, 246144110121111
total = part1(time,distance) 
print(total)