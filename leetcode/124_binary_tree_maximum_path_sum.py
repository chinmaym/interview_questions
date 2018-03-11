'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,
                    1
                   / \
                  2   3
'''



class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxSubPathSum(self,root):
        if root == None:
            return 0
        left = self.maxSubPathSum(root.left)
        right = self.maxSubPathSum(root.right)
        return left + root.val if left > right else right + root.val

    def maxPathSum(self,root,sumList = []):
        if root == None:
            return 0
        sumList.append(root.val+self.maxSubPathSum(root.left)+self.maxSubPathSum(root.right))
        self.maxPathSum(root.left,sumList)
        self.maxPathSum(root.right,sumList)
        return max(sumList)


if __name__=="__main__":
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.left.left = TreeNode(200)
    root.left.right = TreeNode(100)
    root.right = TreeNode(10)
    root.right.right = TreeNode(-25)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)
    print Solution().maxPathSum(root)
