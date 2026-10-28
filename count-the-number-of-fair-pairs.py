class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, 0
        for i in range(n):
            while nums[i] + nums[l] < lower:
                ++l