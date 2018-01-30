'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

Input - 3 9 20 null null 15 7

'''
import math

class Tree():
    def __init__(self):
        pass

    def printZigzag(self,nodeList):
        i = 0;level = 0
    	result = []
    	while i < len(nodeList):
    	    start = i
    	    finish = 2*i
    	    if finish < len(nodeList):
                subList = list(nodeList[start:finish+1])
    	    else:
    		    subList = list(nodeList[start:len(nodeList)+1])
            subList = [int(x) for x in subList if x != 'null']
    	    if level % 2 == 0:
    	        result.append(subList)
    	    else:
    	        subList.reverse()
    	        result.append(subList)
    	    i = finish + 1
    	    level += 1
    	return result


if __name__=="__main__":
    nums = raw_input().split(' ')
    print nums
    print Tree().printZigzag(nums)
