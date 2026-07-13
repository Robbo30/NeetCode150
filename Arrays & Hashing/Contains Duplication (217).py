class Solution(object):
    def containsDuplicate(self, nums):
        # BRUTE FORCE
        # for i, num in enumerate(nums):
        #     for j in range(i + 1, len(nums)):
        #         if num == nums[j]:
        #             return True
        # return False


        # REAL SOLUTION
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False