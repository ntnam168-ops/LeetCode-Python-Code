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

for i in range(1, n):
    x[i] += x[i - 1]
ST = [0] * (4 * n + 5)
lz = [0] * (4 * n + 5)

def build(id, l, r):
    if l == r:
        ST[id] = x[l]
        return
    md = (l + r) // 2
    build(id * 2, l, md)
    build(id * 2 + 1, md + 1, r)
    ST[id] = max(ST[id * 2], ST[id * 2 + 1])

for _ in range(q):
    type = int(data[pos])
    pos += 1
    if type == 1:
        k, u = map(int, data[pos : pos + 2])
        pos += 2
    else:
        a, b = map(int, data[pos : pos + 2])
        pos += 2