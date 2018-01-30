'''
Finding the least common ancestor
		 50
	   /    \
	  30     70
	 /  \   /  \
	20  40 60   80
'''

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class BST():
	def LCA(self,node1Val,node2Val,curNode):
		if curNode == None:
			return None
		if node1Val < curNode.val and curNode.val > node2Val:
			return self.LCA(node1Val,node2Val,curNode.left)
		if node1Val > curNode.val and curNode.val < node2Val:
			return self.LCA(node1Val,node2Val,curNode.right)
		return curNode.val


def main():
	root = Node(50)
	root.left = Node(30)
	root.left.left = Node(20)
	root.left.right = Node(40)
	root.right = Node(70)
	root.right.left = Node(60)
	root.right.right = Node(80)
	print BST().LCA(80,20,root)


if __name__ == '__main__':
	main()
