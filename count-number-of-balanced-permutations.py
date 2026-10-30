dp = [0] * 181
dp[0] = 1

for i in range(1, 10):
    ndp = [0] * 181

    for j in range(181):
        for k in range(9):
            if j + i * k <= 180:
                ndp[j + i * k] += dp[j]

    dp = ndp

print(sum(dp))