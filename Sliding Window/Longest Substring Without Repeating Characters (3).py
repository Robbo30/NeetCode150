class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # O(n^2) SOLUTION

        # max_length = 1
        # for i in range(len(s)):
        #     seen = set()
        #     seen.add(s[i])
        #     for j in range(i + 1, len(s)):
        #         if s[j] not in seen:
        #             seen.add(s[j])
        #             max_length = max(max_length, len(seen))
        #         else:
        #             break
        # return max_length


        # O(n) SOLUTION
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len