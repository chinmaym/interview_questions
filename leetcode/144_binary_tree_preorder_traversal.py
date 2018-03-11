'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
    1
     \
      2
     /
    3
'''


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self,root,traversalList = []):
        if root == None:
            return []
        traversalList.append(root.val)
        self.preorderTraversal(root.left,traversalList)
        self.preorderTraversal(root.right,traversalList)
        return traversalList


if __name__=="__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution().preorderTraversal(root)
