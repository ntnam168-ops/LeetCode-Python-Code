class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        cur = [0] * k

        def back(pos, val):
            if pos == k + 1:
                print(cur)
                return
            
            for i in range(val, n - k + pos + 1):
                cur[pos - 1] = val
                back(pos + 1, i + 1)
        
        back(1, 1)
        return res

s = Solution()
print(s.combine(5, 2))