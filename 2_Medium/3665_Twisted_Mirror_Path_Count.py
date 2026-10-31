class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        dp = [[[0] * 2 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if not i and not j:
                    continue

                if i == 1 and j == 0:
                    dp[i][j][1] = 1
                    continue

                if i == 0 and j == 1:
                    dp[i][j][0] = 1
                    continue

                if j:
                    if grid[i][j - 1] == 0:
                        dp[i][j][0] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod
                    else:
                        dp[i][j][0] = dp[i][j - 1][1]

                if i:
                    if grid[i - 1][j] == 0:
                        dp[i][j][1] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod
                    else:
                        dp[i][j][1] = dp[i - 1][j][0]

        return (dp[n - 1][m - 1][0] + dp[n - 1][m - 1][1]) % mod