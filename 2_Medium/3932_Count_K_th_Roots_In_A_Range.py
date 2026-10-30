class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def f(val):
            if val < 0:
                return -1

            pos = int(val ** (1 / k) + 1)

            if pos ** k > val:
                pos -= 1

            return pos

        return f(r) - f(l - 1)