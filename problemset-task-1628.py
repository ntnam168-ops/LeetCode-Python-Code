import sys

input = sys.stdin.buffer.read

data = list(map(int, input().split()))
n, x = data[:2]
t = data[2:2 + n]

sz = n // 2
a, b = [0], [0]

for v in t[:sz]:
    a += [s + v for s in a]

for v in t[sz:]:
    b += [s + v for s in b]

a.sort()
b.sort()

i, j = 0, len(b) - 1
res = 0

while i < len(a) and j >= 0:
    s = a[i] + b[j]

    if s < x:
        i += 1
    elif s > x:
        j -= 1
    else:
        u, v = a[i], b[j]
        cnt1 = cnt2 = 0

        while i < len(a) and a[i] == u:
            cnt1 += 1
            i += 1

        while j >= 0 and b[j] == v:
            cnt2 += 1
            j -= 1

        res += cnt1 * cnt2

print(res)