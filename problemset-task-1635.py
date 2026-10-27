n, x = map(int, input().split())
ar = list(map(int, input().split()))
dp = [0] * (x + 1)
mod = 10 ** 9 + 7
dp[0] = 1

