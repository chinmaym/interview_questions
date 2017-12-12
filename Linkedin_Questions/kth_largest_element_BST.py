'''Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
'''

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class Tree():
	def __init__(self):
		self.count = 0
		pass
	def get_k_largest(self,node,k):
		if node == None:
			return
		self.get_k_largest(node.right,k)
		self.count += 1
		if self.count > k:
			return
		print "count: ",self.count,", number: ",node.val
		self.get_k_largest(node.left,k)

def main():
	root = Node(50)
	root.left = Node(30)
	root.left.left = Node(20)
	root.left.right = Node(40)
	root.right = Node(70)
	root.right.left = Node(60)
	root.right.right = Node(80)
	Tree().get_k_largest(root,3)

if __name__=="__main__":
	main()