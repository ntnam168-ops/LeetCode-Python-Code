n, x = map(int, input().split())
ar = list(map(int, input().split()))
dp = [0] * (x + 1)
mod = 10 ** 9 + 7
dp[0] = 1
ar.sort()

for i in range(1, x + 1):
    for v in ar:
        if v <= i:
            dp[i] = (dp[i] + dp[i - v]) % mod
        else:
            break
        
print(dp[x])