import sys

input = sys.stdin.buffer.read
write = sys.stdout.write

data = input().split()
pos = 0

n = int(data[pos])
pos += 1
q = int(data[pos])
pos += 1
x = [int(data[i]) for i in range(pos, pos + n)]
pos += n

for _ in range(q):
    type = int(data[pos])
    pos += 1
    