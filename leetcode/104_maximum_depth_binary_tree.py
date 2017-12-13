
class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class Tree():
	def max_depth(self,node):
		if node == None:
			return  0
		left =self.max_depth(node.left)
		right = self.max_depth(node.right)
		return max(left,right) + 1

def main():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.left.left = Node(6)
	print Tree().max_depth(root)


if __name__ == '__main__':
	main()