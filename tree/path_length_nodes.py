'''
program to find path length between node of a binary tree
'''


class Node():
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Tree():
    def pathLength(self,root,val1,val2):
        if root == None:
            return False,0
        if root.val == val1 or root.val == val2:
            return True,1
        left,leftVal = self.pathLength(root.left,val1,val2)
        right, rightVal = self.pathLength(root.right,val1,val2)
        if left and right:
            return False,(leftVal+rightVal)
        elif left or right:
            return True,(leftVal+rightVal+1)
        else:
            return False,(leftVal+rightVal)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right= Node(7)
    root.right.left = Node(6)
    root.left.right = Node(5)
    root.right.left.right = Node(8)
    print Tree().pathLength(root,4,5)[1]
    print Tree().pathLength(root,4,6)[1]
    print Tree().pathLength(root,8,5)[1]


if __name__=="__main__":
    main()
