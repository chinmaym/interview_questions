'''
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \
      4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.max = 0
        pass
    # def getHeight(self, root):
    #     if root is None:
    #         return 0
    #     left = self.getHeight(root.left)
    #     right = self.getHeight(root.right)
    #     return left + 1 if left > right else right + 1
    def getDiameter(self,root):
        if root is None:
            return 0
        leftChild = self.getDiameter(root.left)
        rightChild = self.getDiameter(root.right)
        if leftChild + rightChild > self.max:
            self.max = leftChild + rightChild
        return leftChild + 1 if leftChild > rightChild else rightChild + 1

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    tree = Tree()
    # height = tree.getHeight(root)
    tree.getDiameter(root)
    print tree.max
