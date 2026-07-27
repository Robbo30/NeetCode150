class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        result = ""
        if key not in self.store:
            return result
        
        pairs = self.store[key]
        left = 0
        right = len(pairs) - 1

        while left <= right:
            mid = (right + left) // 2

            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result
        
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)