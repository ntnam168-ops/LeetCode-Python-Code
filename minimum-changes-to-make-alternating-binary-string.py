class Solution:
    def minOperations(self, s: str) -> int:
        s0, s1 = s[:], s[:]
        s0 = list(s0)
        s1 = list(s1)
        for i in range(len(s0)):
            s0[i] = '0' if i & 1 else '1'
        for i in range(len(s1)):
            s1[i] = '1' if i & 1 else '0'
        s0 = "".join(s0)
        s1 = "".join(s1)

        cnt0, cnt1 = 0, 0
        for i in range(len(s)):
            cnt0 += s[i] != s0[i]
            cnt1 += s[i] != s1[i]

        return min(cnt0, cnt1)