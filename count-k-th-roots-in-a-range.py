class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def f(val):
            if val < 0:
                return -1
            pos = val ** (1/ k) + 1
            pos = int(pos)
            if pos ** k > val:
                pos -= 1
            return pos

        return f(r) - f(l - 1)