'''
 Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.
'''

class Node():
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
class Tree():
    def __init__(self):
        pass
    def getLCA(self,node,n,v):
        if node == None:
            return None
        if node.value == n or node.value == v:
            return node.value
        left = self.getLCA(node.left,n,v)
        right = self.getLCA(node.right,n,v)
        if left is not None and right is not None:
            return node.value
        return left or right

def main():
    root = Node(3)
    root.left = Node(5)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    root.right = Node(1)
    root.right.left = Node(0)
    root.right.right = Node(8)
    n,v = input(),input()
    return Tree().getLCA(root,n,v)

if __name__ == '__main__':
    print main()
