class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        total = 0
        nums = list(nums)
        for c in nums:
        	total += ord(c) - ord('0')
        if total & 1:
        	return 0
        return 1
        
s = Solution()
print(s.countBalancedPermutations("123"))
print(s.countBalancedPermutations("112"))
print(s.countBalancedPermutations("12345"))