class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        total = sum(int(c) for c in num)

        if total & 1:
            return 0

        res = 0
        for i0 in range(9):
            for i1 in range(9):
                for i2 in range(9):
                    for i3 in range(9):
                        for i4 in range(9):
                            for i5 in range(9):
                                for i6 in range(9):
                                    for i7 in range(9):
                                        if i1 + 2*i2 + 3*i3 + 4*i4 + 5*i5 + 6*i6 + 7*i7 <= 180:
                                            for i8 in range(9):
                                                if i1 + 2*i2 + 3*i3 + 4*i4 + 5*i5 + 6*i6 + 7*i7 + 8*i8 <= 180:
                                                    for i9 in range(9):
                                                        if i1 + 2*i2 + 3*i3 + 4*i4 + 5*i5 + 6*i6 + 7*i7 + 8*i8 + 9*i9 <= 180:
                                                            res += 1
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break

        return res
s = Solution()
print(s.countBalancedPermutations("123"))
print(s.countBalancedPermutations("112"))
print(s.countBalancedPermutations("12345"))