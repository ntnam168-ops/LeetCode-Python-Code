class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, 0
        res = 0
        
        for i in range(n):
            while l < n and nums[i] + nums[l] < lower:
                l += 1
            while r < n - 1 and nums[i] + nums[r + 1] <= upper:
                r += 1
            res += r - l + 1
            if l <= i and r >= i:
                res -= 1

        return res