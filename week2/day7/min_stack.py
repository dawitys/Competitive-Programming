//TO-DO
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x,self.stack[len(self.stack) - 1][1])))
            
    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1][0]

    def getMin(self):
        return self.stack[len(self.stack) - 1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()