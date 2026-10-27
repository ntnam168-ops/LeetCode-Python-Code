class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i and not j:
                    continue
                if not i:
                    grid[i][j] += grid[i][j - 1]
                elif not j:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[len(grid) - 1][len(grid[0]) - 1]