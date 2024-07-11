class MinStack:

    def __init__(self):
        self.x = list()
        self.min = list()
        
    def push(self, val: int) -> None:
        self.x.append(val)
        if self.min:
            val = min(val, self.min[-1])
        else:
            val = val
        self.min.append(val)

    def pop(self) -> None:
        self.x.pop()
        self.min.pop()

    def top(self) -> int:
        return self.x[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()