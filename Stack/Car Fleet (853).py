class Solution(object):
    def carFleet(self, target, position, speed):
        # O(nlogn) BRUTE FORCE SOLUTION
        #
        # if not position:
        #     return 0

        # cars = sorted(zip(position, speed), reverse=True)
        # fleets = 0
        # times = []
        # for pos, sp in cars:
        #     time = float(target - pos) / sp
        #     times.append(time)

        # i = 0
        # while i < len(times):
        #     fleets += 1
        #     lead_car_time = times[i]
        #     j = i + 1
        #     while j < len(times) and times[j] <= lead_car_time:
        #         j += 1
        #     i = j
        # return fleets


        # O(n) REAL SOLUTION
        if not position:
            return 0

        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, sp in cars:
            time = float(target - pos) / sp
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return(len(stack))
        