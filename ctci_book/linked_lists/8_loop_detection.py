'''
program to detect loops in linked list
'''


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def getloop(root):
    temp1 = temp2 = root

    while not temp2 is None:
        if not temp2.next is None:
            temp2 = temp2.next.next
            temp1 = temp1.next
        else:
            temp2 = temp2.next
        if temp1 == temp2:
            break
    temp = root
    while not temp == temp1:
        temp = temp.next
        temp1 = temp1.next
    return temp.val
def main():
    root = Node('a')
    root.next = Node('b')
    root.next.next = Node('c')
    root.next.next.next = Node('d')
    root.next.next.next.next = Node('e')
    root.next.next.next.next.next = Node('f')
    root.next.next.next.next.next.next = Node('g')
    root.next.next.next.next.next.next.next = root.next.next
    return getloop(root)


if __name__=="__main__":
    print main()
