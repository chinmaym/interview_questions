'''
given a sorted array. create a binary search tree with min height.
'''


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right = None

def createBST(numList,l,h):
    if l>h:
        return None
    mid = (l+h)/2
    root = TreeNode(numList[mid])
    root.left = createBST(numList,l,mid-1)
    root.right = createBST(numList,mid+1,h)
    return root

def traversal(root):
    if root is None:
        return
    print root.val
    traversal(root.left)
    traversal(root.right)

def getHeight(root):
    if root is None:
        return 0
    left = getHeight(root.left)
    right = getHeight(root.right)
    return left+1 if left>right else right+1

def main():
    numList = [1,2,3,4,5,6,7,8,9,10]
    root = createBST(numList,0,len(numList)-1)
    traversal(root)
    print getHeight(root)

if __name__=="__main__":
    main()
