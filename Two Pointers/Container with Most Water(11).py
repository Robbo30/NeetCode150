class Solution(object):
    def maxArea(self, height):
        # O(n^2) SOLUTION
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         max_area = max(max_area, min(height[i], height[j]) * (j - i))
        # return max_area


        # O(n) SOLUTION
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area