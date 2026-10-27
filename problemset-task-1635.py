import sys

input = sys.stdin.read
write = sys.stdout.write
data = input().split()

n = int(data[0])
x = int(data[1])
c = [int(data[i]) for i in range(2, 2 + n)]
c.sort()

dp = [0] * (x + 1)
dp[0] = 1
mod = 10 ** 9 + 7

for i in range(1, x + 1):
    for val in c:
        if val > i:
            break
        dp[i] += dp[i - val]
    dp[i] %= mod

write(str(dp[x]))