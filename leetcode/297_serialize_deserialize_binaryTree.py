'''
    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def serialize(self,root,nodeList = []):
        if root is None:
            nodeList.append(None)
            return
        nodeList.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)


    def deSerialize(self,root,nodeList,i=0):
        if nodeList[i] == None:
            return i+1
        root = Node(nodeList[i])
        i = self.deSerialize(root.left,i+1)
        i = self.deSerialize(root.left,i+1)
        return i+1

    def printTree(self,root):
        if root == None:
            return
        self.printTree(root.left)
        print root.val
        self.printTree(root.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    tree = Tree()
    nodeList = []
    tree.serialize(root,nodeList)
    print nodeList
    node = Node(0)
    tree.deSerialize(node,nodeList)
    tree.printTree(node)

if __name__ == '__main__':
    main()
