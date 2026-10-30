class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_prime = [0] * (n + 1)
        prime = []
        
        def init():
        	for i in range(2, n + 1):
        		if not min_prime[i]:
        			prime.append(i)
        			min_prime[i] = i
        		for x in prime:
        			if x * i > n or x > min_prime[i]:
        				break
        			min_prime[x * i] = x
        
        init()
        for i in range(2, 21):
        	print(i, min_prime[i])
        
s = Solution()
print(s.maximumSum([8, 7, 3, 5, 7, 2, 4, 9]))
print(s.maximumSum([8, 10, 3, 8, 1, 13, 7, 9, 4]))