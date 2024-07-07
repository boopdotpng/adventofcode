def parse_line(line):
  colon = line.find(":")
  ident = int(line[4:colon])
  line = line[colon+2:]

  games = line.split(";")
  red = 0
  green = 0
  blue = 0

  for game in games:
    draws = game.split(',')
    for draw in draws:
      if "red" in draw:
        red = max(int(draw[0:draw.find('r')]), red)
      elif "green" in draw:
        green = max(int(draw[0:draw.find('g')]), green)
      elif "blue" in draw:
        blue = max(int(draw[0:draw.find('b')]), blue)

  print(red, blue, green)
  return red * blue * green 
result = sum([parse_line(line.strip()) for line in open("input.txt", 'r').readlines()])

print(result)