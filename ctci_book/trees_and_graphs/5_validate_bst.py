'''
program to check if a given binary tree is a bst.
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def validateBST(root,min_val = -1,max_val = 2**20):
    if root is None:
        return True
    if (root.val<min_val or root.val>max_val): return False
    return validateBST(root.left,min_val,root.val) and validateBST(root.right,root.val,max_val)

def main():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    print validateBST(root)


if __name__=="__main__":
    main()
