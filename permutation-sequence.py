class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums, gt = [], [1]
        for i in range(1, n + 1):
            nums.append(i)
            gt.append(gt[-1] * i) 
    
        res = []
        for i in range(n):
            d = gt[n - i - 1]
            pos = 0
            while k > d:
                k -= d
                pos += 1
            res.append(nums[pos])
            del nums[pos]

        return res
