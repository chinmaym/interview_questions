'''
print a tree level by level

        1
     2    3
  4   5  6  7
  '''

class tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_level_by_level(root):
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        print node.val
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

if __name__=="__main__":
    root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(5)
    root.right.left = tree(6)
    root.right.right = tree(7)
    get_level_by_level(root)
