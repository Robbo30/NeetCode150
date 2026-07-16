class Solution(object):
    def groupAnagrams(self, strs):
        ordered = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in ordered:
                ordered[sortedString] = []
            ordered[sortedString].append(string)
            

        return list(ordered.values())