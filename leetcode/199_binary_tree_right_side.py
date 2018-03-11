'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
        1
      /   \
     2     3
      \     \
       5     4
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root,level=1,ret=[]):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if level > len(ret):
            ret.append(root.val)
        self.rightSideView(root.right,level+1,ret)
        self.rightSideView(root.left,level+1,ret)
        return ret


if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)

    print Solution().rightSideView(root)
