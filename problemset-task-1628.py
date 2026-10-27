import sys

input = sys.stdin.buffer.read
write = sys.stdout.write
data = input().split()

n, x = map(int, data[0 : 2])
t = list(map(int, data[2 : 2 + n]))

mp1, mp2 = {}, {}
sz1 = n // 2
sz2 = n - sz1

for i in range(1 << sz1):
    s = 0
    for j in range(sz1):
        if (i >> j) & 1:
            s += t[j]
    mp1[s] = mp1.get(s, 0) + 1

for i in range(1 << sz2):
    s = 0
    for j in range(sz2):
        if (i >> j) & 1:
            s += t[sz1 + j]
    mp2[s] = mp2.get(s, 0) + 1

res = 0
for a, b in mp1.items:
    res += b * mp2.get(x - a)

print(res)