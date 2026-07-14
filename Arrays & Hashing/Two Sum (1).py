class Solution(object):
    def twoSum(self, nums, target):
        # BRUTE FORCE
        # for index, i in enumerate(nums):
        #     for j in range(index + 1, len(nums)):
        #         if i + nums[j] == target:
        #             return [index, j]


        # REAL SOLUTION
        seen = {}
        for index, i in enumerate(nums):
            needed = target - i
            if needed in seen:
                return [seen[needed], index]
            seen[i] = index
