class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        n = len(num)
        total = sum(int(c) for c in num)
        
        if total & 1:
        	return 0
        
        dp = [[0] * n for _ in range(total // 2)]
        
        return 1
        
s = Solution()
print(s.countBalancedPermutations("123"))
print(s.countBalancedPermutations("112"))
print(s.countBalancedPermutations("12345"))