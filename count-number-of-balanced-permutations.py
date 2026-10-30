class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        total = 0
        for c in nums:
        	total += ord(c) - ord('0')
        
s = Solution()
print(s.countBalancedPermutations("123"))
print(s.countBalancedPermutations("112"))
print(s.countBalancedPermutations("12345"))