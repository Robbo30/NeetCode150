class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr_streak = 1
                next_num = num + 1
                while next_num in num_set:
                    curr_streak = curr_streak + 1
                    next_num = next_num + 1
                longest_streak = max(longest_streak, curr_streak)

        return longest_streak