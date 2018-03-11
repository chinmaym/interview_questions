'''
program to sort stack
'''

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        if len(self.stack) == 0 or val < self.stack[-1]:
            self.stack.append(val)
        else:
            temp = []
            while len(self.stack)!=0 and val>self.stack[-1]:
                temp.append(self.stack.pop())
            self.stack.append(val)
            while len(temp) != 0 :
                self.stack.append(temp.pop())
    def pop(self):
        return self.stack.pop()


def main():
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(4)
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()

if __name__=="__main__":
    main()
