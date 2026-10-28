class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        pos = [0] * n
        for i in range(n):
            pos[arr[i]] = i
            