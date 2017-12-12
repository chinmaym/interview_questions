
class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None


#--------------- Efficient solution -----------------

def isSymmetric(nodeA,nodeB):
	if not nodeA and not nodeB:
		return True
	elif not nodeA or not nodeB:
		return False
	else:
		return (nodeA.val==nodeB.val) and isSymmetric(nodeA.left,nodeB.right) and isSymmetric(nodeA.right,nodeB.left)

#-------------My Solution------------------
# def isSymmetric(node,side,nodeList):
# 	if node == None:
# 		nodeList.append(-1)
# 		return
# 	nodeList.append(node.val)
# 	if side == "left":
# 		isSymmetric(node.left,side,nodeList)
# 		isSymmetric(node.right,side,nodeList)
# 	else:
# 		isSymmetric(node.right,side,nodeList)
# 		isSymmetric(node.left,side,nodeList)

def main():
	root = Node(1)
	root.left = Node(2)
	# root.left.left = Node(3)
	root.left.right = Node(3)
	root.right = Node(2)
	# root.right.left = Node(5)
	root.right.right = Node(3)
	nodeLeftList = []
	# isSymmetric(root.left,"left",nodeLeftList)
	# nodeRightList = []
	# isSymmetric(root.right,"right",nodeRightList)
	# print nodeLeftList
	# print nodeRightList
	# if len(nodeLeftList) != len(nodeRightList):
	# 	return False
	# for j,i in enumerate(nodeLeftList):
	# 	if i != nodeRightList[j]:
	# 		return False
	# return True
	return isSymmetric(root.left,root.right)

if __name__ == '__main__':
	print main()