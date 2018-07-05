'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   1   7

Target = 9

Output: True

Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.memory = {}
    def twoSum(self,root,val):
        if root is None:
            return False
        result = self.twoSum(root.left,val) or self.twoSum(root.right,val)
        result = result or (True if self.memory.get(root.val) else False)
        self.memory[val-root.val] = 1
        return result

if __name__=="__main__":
    # root = TreeNode(5)
    # root.left = TreeNode(3)
    # root.left.left = TreeNode(2)
    # root.left.right = TreeNode(4)
    # root.right = TreeNode(6)
    # root.right.right = TreeNode(7)
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print Tree().twoSum(root,4)
