class Solution(object):
    def trap(self, height):
        # BRUTE FORCE O(n^2) SOLUTION
        #
        # total_water = 0
        # if not height:
        #     return 0
        # for i in range(len(height)):
        #     left = 0
        #     right = 0
        #     for j in range(0, i + 1):
        #         left = max(left, height[j])
        #     for j in range(i, len(height)):
        #         right = max(right, height[j])
            
        #     total_water += min(left, right) - height[i]
        # return total_water


        # O(n) SOLUTION
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        total_water = 0
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            elif left_max > right_max:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water