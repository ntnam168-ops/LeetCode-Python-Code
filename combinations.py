class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = 1
        for i in range(1, n + 1):
            res *= i
        for i in range(1, k + 1):
            res /= i
        for i in range(1, n - k + 1):
            res /= i
        return res