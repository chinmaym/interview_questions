'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def getPaths(self,root,pathList = [],path = ''):
        print path
        if root == None:
            return None
        if path == '':
            path += str(root.val)
        else:
            path += '->'+str(root.val)
        left = self.getPaths(root.left,pathList,path)
        right = self.getPaths(root.right,pathList,path)
        if not left and not right:
            pathList.append(path)
        return path

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    pathList = []
    Tree().getPaths(root,pathList)
    return pathList


if __name__ == '__main__':
    print main()
