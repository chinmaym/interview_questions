class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.q.append(x)
        if self.minValue > x or self.minValue is None:
            self.minValue = x

    def pop(self):
        """
        :rtype: void
        """
        if len(self.q) == 0:
            return
        num = self.q.pop()
        if num == self.minValue:
            self.minValue = self.top()
            for i in self.q:
                if i < self.minValue:
                    self.minValue = i

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minValue


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
