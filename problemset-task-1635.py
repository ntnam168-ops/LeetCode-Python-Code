import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
x = int(data[1])
c = [int(data[i]) for i in range(2, 2 + n)].sort()

dp = [0] * (x + 1)
mod = 10 ** 9 + 7

for i in range(1, x + 1):
    for 

print(dp[n])