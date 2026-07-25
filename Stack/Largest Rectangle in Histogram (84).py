class Solution(object):
    def largestRectangleArea(self, heights):
        # O(n^2) BRUTE FORCE
        #
        # max_area = 0
        # for i in range(len(heights)):
        #     min_height = heights[i]
        #     for j in range(i, len(heights)):
        #         min_height = min(min_height, heights[j])
        #         area = min_height * (j - i + 1)
        #         max_area = max(max_area, area)
        #
        # return max_area


        # O(n) REAL SOLUTION
        stack = []
        max_area = 0

        for i in range(len(heights)):
            start = i

            while stack and heights[i] < stack[-1][1]:
                start_index, height = stack.pop()
                area = height * (i - start_index)
                max_area = max(max_area, area)
                start = start_index

            stack.append((start, heights[i]))
        
        for start_index, height in stack:
            area = height * (len(heights) - start_index)
            max_area = max(max_area, area)
            
        return max_area
