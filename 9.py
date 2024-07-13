def process_line(line):
    seq = list(map(int, line.split()))
    total = seq[-1]
    while any(seq):
        seq = [b - a for a, b in zip(seq, seq[1:])]
        total += seq[-1]
    return total

print(sum(process_line(line) for line in open("input.txt")))


# part two 
def process_line2(line):
    seq = list(map(int, line.split()))
    total = 0
    m = True 
    while any(seq):
        total += seq[0] * (1 if m else -1)
        seq = [b-a for a,b in zip(seq, seq[1:])]

        m = not m
    return total 

print(sum(process_line2(line) for line in open("input.txt")))