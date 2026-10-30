class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        n = len(num)
        total = sum(int(c) for c in num)
        
        if total & 1:
        	return 0
        
        dp = [[0] * (n // 2 + 1) for _ in range(total // 2 + 1)]
        cnt = [0] * 10
        dp[0][0] = 1
        
        for c in num:
        	cnt[int(c)] += 1
        
        # for val in range(10):
        	# for t in range(cnt[val] + 1):
        		# if t > n // 2:
        			# break
        		# for i in range(total // 2 + 1):
        			# for j in range(t, )
        
        return dp[total // 2][n // 2]
        
s = Solution()
print(s.countBalancedPermutations("123"))
print(s.countBalancedPermutations("112"))
print(s.countBalancedPermutations("12345"))