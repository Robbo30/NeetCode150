class Solution(object):
    def characterReplacement(self, s, k):
        # O(n^2)
        # max_len = 0
        # for i in range(len(s)):
        #     max_freq = 0
        #     count = {}
        #     for j in range(i, len(s)):
        #         count[s[j]] = count.get(s[j], 0) + 1
        #         max_freq = max(max_freq, count[s[j]])
        #         if (j - i + 1) - max_freq <= k:
        #             max_len = max(max_len, j - i + 1) 
        # return max_len