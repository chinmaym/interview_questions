

class Node():
	def __init__(self, value, right = None, left = None):
		self.value = value
		self.right = right
		self.left = left

class Tree():
	def __init__(self):
		pass
	def insert(self, root, value):
		if root == None:
			node = Node(value)
			return node
		if value < root.value:
			if root.left == None:
				root.left = self.insert(None,value)
			else:
				self.insert(root.left,value)
		else:
			if root.right == None:
				root.right = self.insert(None,value)
			else:
				self.insert(root.right,value)

	def delete(self, root, value):
		if root == None:
			return None
		print root.value
		if root.value == value:
			return None
		if root.value < value:
			root.right = self.delete(root.right,value)
			return root
		if root.value > value:
			root.left = self.delete(root.left,value)
			return root

	def printTree(self,root):
		if root is not None:
			self.printTree(root.left)
			print root.value
			self.printTree(root.right)

def main():
	tree = Tree()
	root = tree.insert(None,4)
	tree.insert(root,5)
	tree.insert(root,1)
	tree.insert(root,2)
	tree.insert(root,6)
	tree.printTree(root)
	print "deletion"
	tree.delete(root,6)
	print "after deletion"
	tree.printTree(root)

if __name__=="__main__":
	main()