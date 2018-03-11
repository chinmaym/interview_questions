'''

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level,
except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

'''


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def getHeight(self,root):
        if root is None:
            return 0
        return 1 + self.getHeight(root.left)

    def count(self,root):
        height = self.getHeight(root)
        if height >0:
            if self.getHeight(root.right) == height-1:
                return (1<<(height -1)) + self.count(root.right)
            else:
                return (1<<(height-2)) + self.count(root.left)
        else:
            return 0


if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print Solution().count(root)
