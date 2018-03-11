'''
program to sum two linked lists stored in reverse order.

7->1->6 + 5->9->2 = 2->1->9
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None




def sumNodes(root1,root2):
    ret = sumList = None
    carry = 0
    while (not root1 is None) or (not root2 is None):
        val = root1.val + root2.val + carry
        carry = val / 10
        val = val % 10
        if sumList is None:
            ret = sumList = Node(val)
        else:
            sumList.next = Node(val)
            sumList = sumList.next
        root1 = root1.next
        root2 = root2.next
    while not root1 is None:
        val = root1.val + carry
        carry = val / 10
        val = val %10
        if sumList is None:
            ret = sumList = Node(val)
        else:
            sumList.next = Node(val)
            sumList = sumList.next
        root1 = root1.next
    while not root2 is None:
        val = root2.val + carry
        carry = val / 10
        val = val %10
        if sumList is None:
            ret = sumList = Node(val)
        else:
            sumList.next = Node(val)
            sumList = sumList.next
        root2 = root2.next
    if carry > 0:
        sumList.next = Node(carry)
    return ret

def printNodes(root):
    temp = root
    while not temp.next is None:
        print temp.val,'->',
        temp = temp.next
    print temp.val

def main():
    root1 = Node(8)
    root1.next = Node(6)
    root1.next.next = Node(7)
    root2 = Node(7)
    root2.next = Node(6)
    root2.next.next = Node(2)
    res = sumNodes(root1,root2)
    printNodes(res)

if __name__=="__main__":
    main()
