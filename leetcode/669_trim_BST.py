'''
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2

Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
 '''

class TreeNode:
    def __init__(self,val):
         self.val = val
         self.left = self.right = None

class Tree:
    def trim(self,root,l,r):
        if root is None:
            return None
        if l<= root.val <=r:
            node = TreeNode(root.val)
            node.left = self.trim(root.left,l,r)
            node.right = self.trim(root.right,l,r)
            return node
        elif root.val < l:
            return self.trim(root.right,l,r)
        else:
            return self.trim(root.left,l,r)
    def printTree(self,root):
        if root is None:
            return
        self.printTree(root.left)
        print root.val
        self.printTree(root.right)

if __name__=="__main__":
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.right = TreeNode(4)
    tree = Tree()
    root2 = tree.trim(root,1,3)
    tree.printTree(root2)
