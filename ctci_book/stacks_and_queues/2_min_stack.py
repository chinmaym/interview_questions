'''
implement stack with min value
'''

class Stack:
    def __init__(self):
        self.stack = list()
        self.min = None
    def push(self,val):
        if self.min is None:
            self.min = val
        if val < self.min:
            self.min = val
        self.stack.append(val)
    def findMin(self):
        for i in self.stack:
            if self.min is None:
                self.min = i
            elif i < self.min:
                self.min = i
    def pop(self):
        val = self.stack.pop()
        if val == self.min:
            self.min = None
            self.findMin()
        return val



def main():
    stack = Stack()
    stack.push(2)
    print stack.min
    stack.push(-1)
    print stack.min
    print stack.pop()
    print stack.min

if __name__=="__main__":
    main()
