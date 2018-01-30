
class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class Tree():

	def leastCommonAncestor(self,node1Val,node2Val,curNode,valuePresent):
		if curNode == None:
			return None
		if (curNode.val == node1Val):
			valuePresent[0] = True
			return  curNode
		if (curNode.val == node2Val):
			valuePresent[1] = True
			return curNode
		leftNode = self.leastCommonAncestor(node1Val,node2Val,curNode.left,valuePresent)
		rightNode = self.leastCommonAncestor(node1Val,node2Val,curNode.right,valuePresent)
		if leftNode and rightNode:
			return curNode
		return leftNode if leftNode is not None else rightNode

	def leastCommonAncestor_main(self,node1Val,node2Val,curNode):
		valuePresent = [False,False]
		node = self.leastCommonAncestor(node1Val,node2Val,curNode,valuePresent)
		if valuePresent[0] and valuePresent[1]:
			return node
		else:
			return None


def main():
	root = Node(50)
	root.left = Node(30)
	root.left.left = Node(20)
	root.left.right = Node(40)
	root.right = Node(70)
	root.right.left = Node(60)
	root.right.right = Node(80)
	result = Tree().leastCommonAncestor_main(80,2,root)
	if result:
		print result.val
	else:
		print "Not present"


if __name__ == '__main__':
	main()
