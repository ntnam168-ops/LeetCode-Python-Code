class Solution:
	def minCost(self, grid: list[list[int]]) -> int:
		n = len(grid)
		m = len(grid[0])
		dp = [[set() for _ in range(m)] for _ in range(n)]
		dp[0][0].add(grid[0][0])
		return 1
		
s = Solution()
print(s.minCost([[1, 2], [3, 4]]))
print(s.minCost([[6, 7], [5, 8]]))
print(s.minCost([[2, 7, 5]]))