class Solution:
    def minOperations(self, s: str) -> int:
        s0, s1 = [], []

        for i in range(len(s)):
            s0.append('1' if i & 1 else '0')
            s1.append('0' if i & 1 else '1')

        cnt0 = sum(a != b for a, b in zip(s, s0))
        cnt1 = sum(a != b for a, b in zip(s, s1))

        return min(cnt0, cnt1)