class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        res = nums[n - k:] + nums[:n - k]
        for i in range(n):
            nums[i] = res[i]