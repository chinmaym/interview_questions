'''
 Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Tree:
    def merge(self,root1,root2):
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        node = Node(root1.val + root2.val)
        node.left = self.merge(root1.left, root2.left)
        node.right = self.merge(root1.right, root2.right)
        return node
    def printTree(self,root):
        if root is None:
            return
        self.printTree(root.left)
        print root.val
        self.printTree(root.right)

if __name__=="__main__":
    root1 = Node(1)
    root1.left = Node(3)
    root1.right = Node(2)
    root1.left.left = Node(5)

    root2 = Node(2)
    root2.left = Node(1)
    root2.left.right = Node(4)
    root2.right = Node(3)
    root2.right.right = Node(7)
    tree = Tree()
    root3 = tree.merge(root1,root2)
    tree.printTree(root3)
