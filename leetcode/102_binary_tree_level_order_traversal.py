
class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class Tree():
	def level_order(self, node, levelList, level=1):
		if node == None:
			return 
		if len(levelList)<level:
			levelList.append([])
		levelList[level-1].append(node.val)
		self.level_order(node.left,levelList,level+1)
		self.level_order(node.right,levelList,level+1)

def main():
	root = Node(3)
	root.left = Node(9)
	root.right = Node(20)
	root.right.left = Node(15)
	root.right.right = Node(7)
	levelList = []
	Tree().level_order(root,levelList)
	return levelList


if __name__ == '__main__':
	print main()