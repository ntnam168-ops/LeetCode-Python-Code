import sys

input = sys.stdin.buffer.read
write = sys.stdout.write

data = input().split()
pos = 0

n = int(data[pos])
pos += 1
q = int(data[pos])
pos += 1
x = list(map(int, data[pos : pos + n]))
pos += n

print(n, q)
print(x)

for _ in range(q):
    type = int(data[pos])
    pos += 1
    if type == 1:
        k, u = map(int, data[pos : pos + 2])
        pos += 2
        print(k, u)
    else:
        a, b = map(int, data[pos : pos + 2])
        pos += 2
        print(a, b)