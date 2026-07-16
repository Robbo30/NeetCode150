class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        answer = []
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        for num, count in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            answer.append(num)

        return(answer[:k])