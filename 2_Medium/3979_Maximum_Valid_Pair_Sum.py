class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res, pointer = 0, 0

        for i in range(n):
            if i >= k and nums[i - k] > nums[pointer]:
                pointer = i - k

            if i >= k:
                res = max(res, nums[i] + nums[pointer])

        return res