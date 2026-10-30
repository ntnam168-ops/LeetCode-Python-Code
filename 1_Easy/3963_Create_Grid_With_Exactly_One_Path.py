class Solution:
    def createGrid(self, n: int, m: int) -> list[str]:
        ar = ["#" * m for _ in range(n)]

        for i in range(n):
            ar[i] = list(ar[i])
            ar[i][0] = '.'
            ar[i] = "".join(ar[i])

        ar[n - 1] = "." * m

        return ar