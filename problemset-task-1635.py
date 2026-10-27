n, x = map(int, input().split())
ar = list(map(int, input().split()))
dp = [x + 1] * (x + 1)
dp[0] = 0
mod = 10 ** 9 + 7

for val in ar:
    for i in range(val, x + 1):
        dp[i] = min(dp[i], dp[i - val] + 1)

print(-1 if dp[x] > x else dp[x])