class Solution(object):
    def threeSum(self, nums):
        # BRUTE FORCE
        # result = []
        # n = len(nums)
        # seen_triplets = set()

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 if triplet not in seen_triplets:
        #                     seen_triplets.add(triplet)
        #                     result.append(list(triplet))
        # return result


        nums.sort()
        result = []

        for index, i in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            if index > 0 and i == nums[index - 1]:
                continue
            while left < right:
                three_sum = i + nums[left] + nums[right]
                if three_sum == 0:
                    result.append([i, nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while nums[left] == nums[left - 1] and left < right:
                        left = left + 1
                elif three_sum > 0:
                    right = right - 1
                elif three_sum < 0:
                    left = left + 1
        return result