class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ar = ["#" * m for _ in range(n)]
        for i in range(n):
            ar[i][0] = '.'
        for i in range(m):
            ar[n - 1][i] = '.'
        return ar