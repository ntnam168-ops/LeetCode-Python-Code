class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        pos = -1

        for i in range(len(nums)):
            if nums[i]:
                if pos >= 0 and i - pos - 1 < k:
                    return False
                pos = i

        return True