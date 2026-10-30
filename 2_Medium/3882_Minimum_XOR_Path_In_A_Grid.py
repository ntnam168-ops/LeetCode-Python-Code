class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[set() for _ in range(m)] for _ in range(n)]
        dp[0][0].add(grid[0][0])

        for i in range(n):
            for j in range(m):
                if not i and not j:
                    continue

                if i:
                    for val in dp[i - 1][j]:
                        dp[i][j].add(val ^ grid[i][j])

                if j:
                    for val in dp[i][j - 1]:
                        dp[i][j].add(val ^ grid[i][j])

        return min(dp[n - 1][m - 1])