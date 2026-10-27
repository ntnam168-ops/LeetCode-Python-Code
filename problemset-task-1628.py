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
    print(s)