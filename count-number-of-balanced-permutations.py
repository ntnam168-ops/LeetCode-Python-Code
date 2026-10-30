class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        n = len(num)
        total = sum(int(c) for c in num)
        if total & 1:
        	return 0
        dp = [[0] * (n // 2 + 1) for _ in range(total // 2 + 1)]
        gt = [0] * (n + 1)
        inv = [0] * (n + 1)
        cnt = [0] * 10
        dp[0][0] = 1

        def pw(a, b):
            res = 1
            while b:
                if b & 1:
                    res = (res * a) % mod
                a = (a * a) % mod
                b //= 2
            return res
            
        def init():
            gt[0] = 1
            for i in range(1, n + 1):
                gt[i] = (gt[i - 1] * i) % mod
            inv[n] = pw(gt[n], mod - 2)
            for i in range(n, 0, -1):
                inv[i - 1] = (inv[i] * i) % mod
                
        # def init():
        	# gt[0] = 1
        	# for i in range(1, n + 1):
        		# gt[i] = (gt[i - 1] * i) % mod
        	# inv[n] = pw(gt[n], mod - 2)
            # for i in range(n, 0, -1):
                # inv[i - 1] = (inv[i] * i) % mod
        
        init()
        for c in num:
        	cnt[int(c)] += 1
        # for val in range(10):
        	# for t in range(cnt[val] + 1):
        		# if t > n // 2:
        			# break
        		# for i in range(total // 2 + 1):
        			# for j in range(t, )
        return dp[total // 2][n // 2]