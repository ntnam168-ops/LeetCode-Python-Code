class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            md = (l + r) // 2
            if (md + 1) * (md + 1) <= x:
                l = md + 1
            else:
                r = md
        return l