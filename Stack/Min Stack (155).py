class MinStack(object):
    # BRUTE FORCE O(n) for getMin() SOLUTION
    # def __init__(self):
    #     self.stack = []

    # def push(self, value):
    #     self.stack.append(value)
        

    # def pop(self):
    #     self.stack.pop()
        

    # def top(self):
    #     return self.stack[-1]
        

    # def getMin(self):
    #     return min(self.stack)



    # REAL SOLUTION O(1)
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            curr_min = min(value, self.min_stack[-1])
            self.min_stack.append(curr_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()        

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]