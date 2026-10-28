class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = n - 1, n - 1
        res = 0
        
        for i in range(n):
            while l > 0 and nums[i] + nums[l - 1] >= lower:
                l -= 1
            while r > 0 and nums[i] + nums[r] > upper:
                r -= 1
            if nums[i] + nums[l] < lower or nums[i] + nums[r] > upper:
                continue
            res += r - l + 1
            if l <= i and r >= i:
                res -= 1

        return res // 2