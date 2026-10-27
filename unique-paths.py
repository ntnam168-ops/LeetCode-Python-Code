class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not i or not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]