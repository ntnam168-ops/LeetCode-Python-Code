class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pos = {}
        for i, x in enumerate(nums):
            if target - x in pos:
                return [pos[target - x], i]
            pos[x] = i