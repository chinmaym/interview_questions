'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.levelSum = []
        self.levelCount = []
    def averageLevels(self,root,l=0):
        if root is None:
            return None
        if len(self.levelSum) >= l+1:
            self.levelSum[l] += root.val
            self.levelCount[l] += 1
        else:
            self.levelSum.append(root.val)
            self.levelCount.append(1)
        self.averageLevels(root.left,l+1)
        self.averageLevels(root.right,l+1)

    def getResult(self,root):
        self.averageLevels(root)
        self.levelAverage = []
        for i in range(len(self.levelSum)):
            self.levelAverage.append(self.levelSum[i]*1.0/self.levelCount[i])
        return self.levelAverage

if __name__=="__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    tree = Tree()
    print tree.getResult(root)
