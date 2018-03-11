'''
given a tree, create linked list of nodes at each depth.
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def createLinkedList(root,dList,level = 0):
    if root is None:
        return
    if level<=len(dList)-1:
        temp = dList[level]
        while not temp.next is None:
            temp = temp.next
        temp.next = Node(root.val)
    else:
        dList.append(Node(root.val))
    createLinkedList(root.left,dList,level+1)
    createLinkedList(root.right,dList,level+1)
    return

def printNodeList(dList):
    for i in dList:
        temp = i
        while not temp.next is None:
            print temp.val,"->",
            temp = temp.next
        print temp.val
def main():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    dList = []
    createLinkedList(root,dList)
    printNodeList(dList)

if __name__=="__main__":
    main()
