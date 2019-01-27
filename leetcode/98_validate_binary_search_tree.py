'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

Input:
    2
   / \
  1   3
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def validateBST(root, min, max):
    if root is None:
        return True
    if root.val > min and root.val < max:
        return validateBST(root.left, min, root.val) and validateBST(root.right, root.val, max)
    else:
        return False

if __name__=="__main__":
    root = Node(5)
    root.left = Node(1)
    root.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(6)
    print validateBST(root, -1000, 10000)
