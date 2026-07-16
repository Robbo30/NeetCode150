class Solution(object):
    def productExceptSelf(self, nums):
        # BRUTE FORCE
        # curr_product = 1
        # products = []
        # for index, i in enumerate(nums):
        #     curr_product = 1
        #     for indexj, j in enumerate(nums):
        #         if index != indexj:
        #             curr_product = curr_product * j
        #     products.append(curr_product)
        
        # return products


        # REAL SOLUTION
        output = len(nums) * [1] 
        left_product = 1
        for i in range(len(nums)):
            output[i] = left_product
            left_product = left_product * nums[i]

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * right_product
            right_product = right_product * nums[i]
        
        return output