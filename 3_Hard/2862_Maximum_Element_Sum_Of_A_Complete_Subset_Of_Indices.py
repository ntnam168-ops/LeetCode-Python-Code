class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        n = len(nums)
        min_prime = [0] * (n + 1)
        ans = [0] * (n + 1)
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

        for i in range(1, n + 1):
            val = i
            cur = 1

            while val > 1:
                u = min_prime[val]
                cnt = 0

                while val % u == 0:
                    val //= u
                    cnt += 1

                if cnt & 1:
                    cur *= u

            ans[cur] += nums[i - 1]

        return max(ans)