n, x = map(int, input().split())
ar = list(map(int, input().split()))
dp = [0] * (x + 1)
mod = 10 ** 9 + 7
dp[0] = 1

for i in range(1, x + 1):
    for x in ar:
        if x <= i:
            dp[i] = (dp[i] + dp[i - x]) % mod
    for j in range(1, x + 1):
        print(dp[j], end = " ")
    print()

print(dp[x])

