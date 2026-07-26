class Solution(object):
    def searchMatrix(self, matrix, target):
        # O(n^2) BRUTE FORCE
        #
        # for i in matrix:
        #     for j in i:
        #         if j == target:
        #             return True
        # return False


        # O(log(m * n)) REAL SOLUTION
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            cols = len(matrix[0])
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
        return False
