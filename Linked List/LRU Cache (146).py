# class LRUCache(object):

#     def __init__(self, capacity):
    # O(n) SPACE BRUTE FORCE
    #
    #     self.cache = []
    #     self.capacity = capacity
        

    # def get(self, key):
    #     for i in range(len(self.cache)):
    #         if self.cache[i][0] == key:
    #             temp = self.cache.pop(i)
    #             self.cache.append(temp)
    #             return temp[1]
    #     return -1
        

    # def put(self, key, value):
    #     for i in range(len(self.cache)):
    #         if self.cache[i][0] == key:
    #             temp = self.cache.pop(i)
    #             temp[1] = value 
    #             self.cache.append(temp)
    #             return
    
    #     if len(self.cache) >= self.capacity: # evicts oldest item if at max capacity
    #         self.cache.pop(0)
        
    #     self.cache.append([key, value]) # add new item to the end


# O(1) SPACE REAL SOLUTION
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()     

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)