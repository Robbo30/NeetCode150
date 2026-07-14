class Solution(object):
    def isAnagram(self, s, t):
        # O(N log N) APPROACH
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        # REAL SOLUTION -- O(N)
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}
        for charS in s:
            if charS not in countS:
                countS[charS] = 1
            else:
                countS[charS] += 1

        for charT in t:
            if charT not in countT:
                countT[charT] = 1
            else:
                countT[charT] += 1

        return countS == countT