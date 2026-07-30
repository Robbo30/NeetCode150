class Solution(object):
    def findDuplicate(self, nums):
        # O(n) SPACE BRUTE FORCE
        #
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)



        # O(1) SPACE REAL SOLUTION
        slow = 0
        fast = 0

        while True: # Part 1: loop for inner loop collision point
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Part 2: find the cycle entrance / duplicate
        slow2 = 0
        while True:
            if slow == slow2: # For a cycle the distance from the start of the list to the cycle entrance is always equal to the distance from the collision point to the cycle entrance
                return slow
            slow = nums[slow]
            slow2 = nums[slow2] # So by moving both forward at the same speed, they are guranteed to meet right at the entrance point which shows the repeated number