'''
program to check whether the tree t1 is a subtree of t2
'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def check(root1,root2):
    if not (root1 or root2):
        return True
    elif not root1:
        return False
    elif not root2:
        return False
    return (root1.val == root2.val) and check(root1.left,root2.left) and check(root1.right,root2.right)



def checkSubTree(root1,root2):
    visited = []
    q = [root1]
    while len(q)!=0:
        node = q.pop(0)
        visited.append(node)
        if node.val == root2.val:
            checkTree = check(node,root2)
            if checkTree:
                return True
        for i in [node.left,node.right]:
            if i and i not in visited:
                q.append(i)
    return False


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
    root2 = TreeNode(3)
    root2.right = TreeNode(4)
    # root2.right.right = TreeNode(5)
    print checkSubTree(root,root2)



if __name__=="__main__":
    main()
