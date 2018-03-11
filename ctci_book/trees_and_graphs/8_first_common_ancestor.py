'''
program to  find the first common ancestor in a  binary tree.
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def findAncestor(root,val1,val2):
    if root is None:
        return None
    if root.val == val1 or root.val == val2: return root.val
    left = findAncestor(root.left,val1,val2)
    right = findAncestor(root.right,val1,val2)
    if left and right: return root.val
    return left or right


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
    return findAncestor(root,9,7)


if __name__=="__main__":
    print main()
