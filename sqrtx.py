class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l < r:
            md = (l + r) // 2
            if (md + 1) ** 2 <= x:
                l = md + 1
            else:
                r = md
        return l
s = Solution()
print(s.mySqrt(10))