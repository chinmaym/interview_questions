"""
 A linked list is given such that each node contains an additional random pointer
 which could point to any node in the list or null.

Return a deep copy of the list.
"""

class RandomListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def deepCopy(head):
    root = head
    while root:
        temp = RandomListNode(root.val)
        temp.next = root.next
        root.next = temp
        root = temp.next
    root = head
    newRoot = head.next
    while newRoot.next:
        newRoot.random = root.random.next
        root = newRoot.next
        newRoot = root.next
    newRoot.random = root.random.next
    res = newRoot = head.next
    root = head
    while newRoot.next:
        root.next = newRoot.next
        newRoot.next = newRoot.next.next
        newRoot = newRoot.next
    root.next = newRoot.next
    return res

def printList(head):
    root = head
    while root.next:
        print (root.val, root.random.val), "->",
        root = root.next
    print (root.val, root.random.val)

if __name__=="__main__":
    one = RandomListNode(1)
    two = RandomListNode(2)
    three = RandomListNode(3)
    four = RandomListNode(4)
    one.next = two
    one.random = three
    two.next = three
    two.random = one
    three.next = four
    three.random = one
    four.random = two
    print "original"
    printList(one)
    newList = deepCopy(one)
    print "copy"
    printList(newList)
