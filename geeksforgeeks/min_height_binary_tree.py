
class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class Tree():
	def min_height(self,node):
		if node == None:
			return None
		left = self.min_height(node.left)
		right = self.min_height(node.right)
		if left and right:
			return min(left,right)+1
		elif left:
			return left+1
		elif right:
			return right+1
		else:
			return 1

def main():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	print Tree().min_height(root)

if __name__ == '__main__':
	main()