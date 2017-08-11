
'''*******  My Solution  *********'''
def twoSum(num_list,target):
	num_dict={}
	for n,i in enumerate(num_list):
		diff = target - i
		if num_dict.get(diff) is not None and num_dict.get(diff)!=n:
			return [num_dict[diff],n]
		else:
			num_dict[i] = n


# '''*******  My Solution  2*********'''

# def twoSum(numList, target):
# 	diffDict = []
# 	for n,i in enumerate(numList):
# 		if i in diffList:
# 			return [diffList.index(i),n]
# 		else:
# 			diffList.append(target-i)



if __name__=="__main__":
	num_list = map(int,raw_input().split())
	target = input()
	print twoSum(num_list,target)