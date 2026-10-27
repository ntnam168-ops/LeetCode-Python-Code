class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        for i in range(n):
            