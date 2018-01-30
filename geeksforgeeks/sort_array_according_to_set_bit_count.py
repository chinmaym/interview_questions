'''
Input: arr[] = {5, 2, 3, 9, 4, 6, 7, 15, 32};
Output: 15 7 5 3 9 6 2 4 32
'''
def getBitCount(num):
	count = 0
	while num:
		if num&1:
			count+=1
		num>>=1
	return count

def main():
	nums = [5, 2, 3, 9, 4, 6, 7, 15, 32]
	bitCountList = [[] for _ in range(33)]
	for i in nums:
		bitCount = getBitCount(i)
		bitCountList[bitCount].append(i)
	for i in range(len(bitCountList)-1,-1,-1):
		if len(bitCountList[i])>0:
			for j in bitCountList[i]: print j,

if __name__=="__main__":
	main()
