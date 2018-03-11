'''
program to find if two linked lists intersect
'''
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def getIntersection(root1,root2):
    temp1 = root1
    temp2 = root2
    count = 0
    while (not temp1 is None) and (not temp2 is None):
        if temp1 == temp2:
            return temp1.val
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1 is None:
        temp = root2
        temp3 = root1
        while not temp2 is None:
            temp2 = temp2.next
            temp = temp.next
    elif temp2 is None:
        temp = root1
        temp3 = root2
        while not temp1 is None:
            temp1 = temp1.next
            temp = temp.next
    while not temp.val == temp3.val:
        temp = temp.next
        temp3 = temp3.next
    return  temp.val


def main():
    root1 = Node('a')
    root1.next = Node('b')
    root1.next.next = Node('c')
    root1.next.next.next = Node('d')
    root2 = Node('z')
    root2.next = Node('x')
    root2.next.next = Node('y')
    root2.next.next.next = root1.next.next
    return getIntersection(root1,root2)

if __name__=="__main__":
    print main()
