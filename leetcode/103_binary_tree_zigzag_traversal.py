"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getArray(root, arr, level = 1):
    if root is None:
        return
    if len(arr) < level:
        arr.append([])
    if level % 2 != 0:
        arr[level-1].append(root.val)
    else:
        temp = [root.val]
        temp.extend(arr[level-1])
        arr[level-1] = temp
    getArray(root.left, arr, level+1)
    getArray(root.right, arr, level+1)
    return

if __name__=="__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    arr = []
    getArray(root, arr)
    print arr
