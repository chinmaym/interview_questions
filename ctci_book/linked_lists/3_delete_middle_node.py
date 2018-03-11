'''
program to delete the middle node.
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def middle_delete(root):
    if root is None:
        return root
    temp1 = temp2 = root
    while not temp2 is None:
        if not temp2.next is None:
            temp2 = temp2.next.next
            temp1 = temp1.next
        else:
            temp2 = temp2.next
    temp = root
    while not temp.next == temp1:
        temp = temp.next
    temp.next = temp1.next
    return root

def printNodes(root):
    temp = root
    while not temp.next is None:
        print temp.val,"->",
        temp = temp.next
    print temp.val
def main():
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)
    root.next.next.next.next.next = Node(6)
    printNodes(root)
    root = middle_delete(root)
    printNodes(root)

if __name__=="__main__":
    main()
