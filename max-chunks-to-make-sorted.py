class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        pos = [0] * n
        for i in range(n):
            pos[arr[i]] = i

        res, val = 0, 0
        for i in range(n):
            val = max(val, pos[i])
            res += val == i
        return res