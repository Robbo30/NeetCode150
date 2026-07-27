class Solution(object):
    def findMin(self, nums):
        # O(n) BRUTE FORCE
        # min_val = nums[0]

        # for num in nums:
        #     min_val = min(min_val, num)
        
        # return min_val


        # O(log n ) REAL SOLUTION
        left = 0 
        right = len(nums) - 1
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return res
