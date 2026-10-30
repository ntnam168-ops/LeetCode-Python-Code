class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_prime = [0] * (n + 1)
        
s = Solution()
print(s.maximumSum([8,7,3,5,7,2,4,9]))
print(s.maximumSum([8,10,3,8,1,13,7,9,4]))