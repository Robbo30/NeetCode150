class Solution(object):
    def dailyTemperatures(self, temperatures):
        # O(n^2) BRUTE FORCE SOLUTION
        #
        # n = len(temperatures)
        # res = []
        # for i in range(n):
        #     count = 1
        #     j = i + 1
        #     while j < n: 
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         j += 1
        #         count += 1
        #     if j == n:
        #         count = 0
        #     res.append(count)
        # return res


        # O(n) SOLUTION
        res = len(temperatures) * [0]
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append((temp, index))
        return res
