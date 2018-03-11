'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


'''


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self,root):
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 :
            return right+1
        elif right == 0:
            return left+1
        else:
            return left+1 if left<right else right+1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print Solution().minDepth(root)
