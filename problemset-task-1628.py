import sys

input = sys.stdin.buffer.read
write = sys.stdout.write
data = input().split()

n, x = map(int, data[0 : 2])
t = list(map(int, data[2 : 2 + n]))

sz1 = n // 2
sz2 = n - sz1
mp1, mp2 = [0], [0]

for v in t[:sz1]:
    mp1 += [a + v for a in mp1]
for v in t[sz1 : n]:
    mp2 += [a + v for a in mp2]

mp1.sort()
mp2.sort()
