class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums, gt = [], [1]
        for i in range(1, n + 1):
            nums.append(i)
            gt[i] = gt[-1] * i
        print(gt)

s = Solution()
print(s.getPermutation(4, 9))
