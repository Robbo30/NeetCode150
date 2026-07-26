class Solution(object):
    def minEatingSpeed(self, piles, h):
        # O(m * n) BRUTE FORCE
        #
        # k = 1
        # while True:
        #     total_hours = 0
        #     for pile in piles:
        #         total_hours += math.ceil(float(pile) / k)
        #     if total_hours <= h:
        #         return k
        #     elif total_hours > h:
        #         k += 1
        # return k


        # REAL SOLUTION
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:
                result = mid
                right = mid - 1
            elif total_hours > h:
                left = mid + 1

        return result