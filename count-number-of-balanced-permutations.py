class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        total = sum(int(c) for c in num)
        
        if total & 1:
        	return 0
 		return res
s = Solution()
print(s.countBalancedPermutations("123"))
print(s.countBalancedPermutations("112"))
print(s.countBalancedPermutations("12345"))