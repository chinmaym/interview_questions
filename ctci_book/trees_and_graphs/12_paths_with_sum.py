'''
program to find the number of paths in a tree that sum upto a given sum
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def checkSum(root,totSum = 0):
    if root is None:
        return 0
    if totSum-root.val == 0:
        return 1
    else:
        return checkSum(root.left,totSum-root.val) + checkSum(root.right,totSum-root.val)


def getPathsNum(root,totSum):
    visited = []
    q = [root]
    count = 0
    while len(q)!= 0:
        node = q.pop(0)
        count += checkSum(node,totSum)
        visited.append(node)
        for i in [node.left,node.right]:
            if i and i not in visited:
                q.append(i)
    return count

def main():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    print getPathsNum(root,7)

if __name__=="__main__":
    main()
