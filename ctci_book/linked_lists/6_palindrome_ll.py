'''
check if the linked list is palindrome.
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def checkPalindrome(root):
    stack = []
    temp1 = temp2 = root
    while not temp1 is None:
        if not temp1.next is None:
            stack.append(temp2.val)
            temp1 = temp1.next.next
            temp2 = temp2.next
        else:
            temp1 = temp1.next
    temp2 = temp2.next
    while not temp2 is None:
        val = stack.pop()
        if val != temp2.val:
            return False
        temp2 = temp2.next
    return True

def main():
    root = Node('p')
    root.next = Node('a')
    root.next.next = Node('w')
    root.next.next.next = Node('a')
    root.next.next.next.next = Node('p')
    root.next.next.next.next.next = Node('q')
    return checkPalindrome(root)


if __name__=="__main__":
    print main()
