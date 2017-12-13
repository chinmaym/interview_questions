'''
Given an array of n elements, the task is to find the greatest number such that it is product of two elements of given array. 
If no such element exists, print -1. 

Input :  A[] = {10, 3, 5, 30, 35}
Output:  30
Explanation: 30 is the product of 10 and 3.

Input :  A[] = {2, 5, 7, 8}
Output:  -1
Explanation: Since, no such element exists.

Input :  A[] = {10, 2, 4, 30, 35}
Output:  -1

Input :  A[] = {10, 2, 2, 4, 30, 35}
Output:  4

'''
def main():
	nums = [2, 5, 7, 8]
	numDict = {}
	maxProduct = -1
	for i in nums:
		if numDict.get(i):
			if maxProduct<(i*max(numDict[i])):
				maxProduct = i*max(numDict[i])
		for j in nums:
			if i == j:
				continue
			q = j/i
			if q:
				if not numDict.get(q):
					numDict[q] = []
				numDict[q].append(i)
	return maxProduct

if __name__=="__main__":
	print main()