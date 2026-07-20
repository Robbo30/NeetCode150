class Solution(object):
    def characterReplacement(self, s, k):
        # O(n^2) SOLUTION
        #
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


        # O(n) SOLUTION
        left = 0
        freqs = {}
        window_len = 0
        max_freq = 0
        replacements = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
            
            max_freq = max(max_freq, freqs[char])
            window_len = right - left + 1
            replacements = window_len - max_freq
            if replacements > k:
                freqs[s[left]] -= 1
                left += 1
                window_len = right - left + 1
                replacements = window_len - max_freq
            max_len = max(max_len, window_len)
        return max_len