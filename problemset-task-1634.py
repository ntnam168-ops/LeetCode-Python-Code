n, x = map(int, input().split())
ar = list(map(int, input().split()))
dp = [1e9] * (x + 1)

for val in ar:
    for i in range(val, x + 1):
        dp[i] = min(dp[i], dp[i - x] + 1)

print(-1 if dp[x] == 1e9 else dp[x])