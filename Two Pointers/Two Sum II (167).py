class Solution(object):
    def twoSum(self, numbers, target):
        # BRUTE FORCE
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []


        # O(N) Solution
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1 
        return False
