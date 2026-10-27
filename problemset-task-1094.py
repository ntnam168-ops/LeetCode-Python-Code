n = int(input())
ar = list(map(int, input().split()))
res = 0
for i in range(1, n):
    res += max(0, ar[i - 1] - ar[i])
    ar[i] = max(ar[i], ar[i - 1])
print(res)