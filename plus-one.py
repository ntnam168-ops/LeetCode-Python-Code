class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        list[-1] += 1
        for i in range(len(list) - 1, 0, -1):
            if list[i] == 10:
                list[i] = 0
                list[i - 1] += 1
        if list[0] == 10:
            list[0] = 0
            list = [1] + list
        return list