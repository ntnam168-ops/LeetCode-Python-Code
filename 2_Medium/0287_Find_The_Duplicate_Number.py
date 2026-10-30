class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        mp = {}

        for val in nums:
            mp[val] = mp.get(val, 0) + 1
            if mp[val] > 1:
                return val