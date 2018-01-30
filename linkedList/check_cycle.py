'''
Program to find cycles in a linked list.
'''


class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def checkCycle(root,slow = None,fast = None):
    if slow == None and fast == None:
        slow = fast = root
    elif fast == None:
        return False
    elif slow == fast:
        return True
    elif fast.next == None:
        return False
    return checkCycle(root,slow.next,fast.next.next)

def main():
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)
    root.next.next.next.next.next = root.next.next
    print checkCycle(root)


if __name__=="__main__":
    main()
