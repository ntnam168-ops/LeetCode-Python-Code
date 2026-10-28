class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res, pointer = 0, 0
        for i in range(n):
        	while i >= k:
        		if nums[i - k] > nums[pointer]:
        			pointer = i - k
        	res = max(res, a[i] + a[pointer])
        return res
        
s = Solution()
print(s.maxValidPairSum([1, 2, 3, 4], 2))