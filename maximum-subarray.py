class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        nums = [0] + nums
        for i in range(1, n + 1):
            nums[i] += nums[i - 1]
        res, mn = 0, 0
        for i in range(1, n + 1):
            res = max(res, nums[i] - mn)
            mn = min(mn, nums[i])
        return res