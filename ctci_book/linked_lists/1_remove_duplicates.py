'''
Code to remove duplicates from an unsorted linked list.
'''


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def removeDuplicates(root,valDict={}):
    if root is None:
        return None
    if valDict.get(root.val) is None:
        valDict[root.val] = 1
        root.next = removeDuplicates(root.next,valDict)
    else:
        return root.next
    return root

def printNodes(root):
    temp = root
    while temp.next:
        print temp.val,"->",
        temp = temp.next
    print temp.val

def main():
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(1)
    root.next.next.next.next = Node(4)
    printNodes(root)
    removeDuplicates(root)
    printNodes(root)

if __name__=="__main__":
    main()
