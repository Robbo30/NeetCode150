class Solution(object):
    def maxProfit(self, prices):
        # O(n^2) SOLUTION
        #
        # max_profit = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j]
        #         max_profit = max(max_profit, sell - buy)
        # return max_profit


        # O(n) SOLUTION
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right 
            right += 1
        return max_profit