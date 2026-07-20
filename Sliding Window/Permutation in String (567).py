class Solution(object):
    def checkInclusion(self, s1, s2):
        #O (n^3logn) BRUTE FORCE SOLUTION
        #
        # s1 = sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         sub_str = s2[i : j + 1]
        #         sub_str = sorted(sub_str)
        #         if sub_str == s1:
        #             return True
        # return False


        # O(n) SOLUTION
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            right_index = ord(s2[right]) - ord("a")
            s2_count[right_index] += 1
            if s1_count[right_index] == s2_count[right_index]:
                matches += 1
            elif s1_count[right_index] + 1 == s2_count[right_index]:
                matches -= 1
            
            left_index = ord(s2[left]) - ord("a")
            s2_count[left_index] -= 1
            if s1_count[left_index] == s2_count[left_index]:
                matches += 1
            elif s1_count[left_index] - 1 == s2_count[left_index]:
                matches -= 1
            
            left += 1
        return matches == 26
