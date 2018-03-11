'''
program to check if the binary tree is balanced.
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def getHeight(root):
    if root is None:
        return 0
    left = getHeight(root.left)
    right = getHeight(root.right)
    return  left+1 if left >right else right+1

def checkBalanced(root):
    if root == None:
        return True
    left = checkBalanced(root.left)
    right = checkBalanced(root.right)
    if left == False or right == False:
        return False
    left = getHeight(root.left)
    right = getHeight(root.right)
    if abs(left-right)>1:
        return False
    else:
        return True

def main():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(0)
    # root.left.right = TreeNode(3)
    # root.left.right.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    print checkBalanced(root)
if __name__=="__main__":
    main()
