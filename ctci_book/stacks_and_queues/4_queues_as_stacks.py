'''
implement queues as 2 stacks
'''


class Myqueue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
    def queue(self,val):
        self.stack1.append(val)
    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

def main():
    q = Myqueue()
    q.queue(1)
    q.queue(2)
    q.queue(3)
    q.queue(4)
    print q.dequeue()
    q.queue(5)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()


if __name__=="__main__":
    main()
