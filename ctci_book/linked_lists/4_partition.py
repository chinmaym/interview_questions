'''
program to partition the linked list around a certain value.

 input = 3->5->8->5->10->2->1
 output = 3->1->2->10->5->5->8

 '''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def partition(root,k):
    before = after = None
    beforeRoot = afterRoot = None
    temp = root
    while not temp is None:
        if temp.val < k :
            if not before is None:
                before.next = temp
                before = before.next
            else:
                before = temp
                beforeRoot = before
            temp = temp.next
            before.next = None
        else:
            if not after is None:
                after.next = temp
                after = after.next
            else:
                after = temp
                afterRoot = after
            temp = temp.next
            after.next = None
    before.next = afterRoot
    return beforeRoot

def printNodes(root):
    temp = root
    while not temp.next is None:
        print temp.val,'->',
        temp = temp.next
    print temp.val

def main():
    root = Node(3)
    root.next = Node(5)
    root.next.next = Node(8)
    root.next.next.next = Node(5)
    root.next.next.next.next = Node(10)
    root.next.next.next.next.next = Node(2)
    root.next.next.next.next.next.next = Node(1)
    printNodes(root)
    root = partition(root,5)
    printNodes(root)

if __name__=="__main__":
    main()
