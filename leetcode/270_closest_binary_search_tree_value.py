'''
Given a binary search tree and a target node K.
The task is to find the node with minimum absolute difference with given target value K.
           9
         /    \
        4     17
       / \      \
      3   6     22
         / \    /
        5   7  20

Examples:

// For above binary search tree
Input  :  k = 4
Output :  4

Input  :  k = 18
Output :  17

Input  :  k = 12
Output :  9
'''

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def getClosestValue(self,root,val):
        if root == None:
            return None,None
        if root.val == val:
            return root.val,0
        diff = abs(root.val - val)
        if val < root.val:
            childKey, childDiff = self.getClosestValue(root.left,val)
        else:
            childKey, childDiff = self.getClosestValue(root.right,val)
        if childDiff is not None and childDiff < diff:
            return  childKey,childDiff
        else:
            return root.val,diff

def main():
    root = Node(9)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(7)
    root.right = Node(17)
    root.right.right = Node(22)
    root.right.right.left = Node(20)
    userVal = input()
    return Tree().getClosestValue(root,userVal)[0]

if __name__ == '__main__':
    print main()
