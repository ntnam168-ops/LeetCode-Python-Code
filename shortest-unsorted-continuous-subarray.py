class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        ar = nums[:]
        ar.sort()
        if ar == nums:
            return 0
        for i in range(len(nums)):
            if (nums[i] != ar[i]):
                for j in range(len(nums) - 1, -1, -1):
                    if (nums[j] != ar[j]):
                        return j - i + 1