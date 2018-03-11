'''
return kth element from the last in singly linked list.
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def kth_from_last(root,k):
    temp2 = temp1 = root
    while k>0:
        if not temp2 is None:
            temp2 = temp2.next
        else:
            return -1
        k-=1
    while not temp2 is None:
        temp1 = temp1.next
        temp2 = temp2.next
    return temp1.val

def main():
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)
    return kth_from_last(root,1)

if __name__=="__main__":
    print main()
