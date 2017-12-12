'''
LCS of AGGTAB and GXTXAYB is GTAB

AGGTAB
GXTXAYB
'''

def longest_common_subsequence(strA,strB):
	aLen = len(strA)
	bLen = len(strB)
	table = [[0 for _ in range(bLen+1)] for _ in range(aLen+1)]
	for i in range(aLen+1):
		for j in range(bLen+1):
			if i==0 or j==0:
				table[i][j] = 0
			elif strA[i-1] == strB[j-1]:
				table[i][j] = table[i-1][j-1] + 1
			else:
				table[i][j] = max(table[i-1][j],table[i][j-1])

	finalLength = table[aLen][bLen]
	finalStr = []
	i = aLen; j=bLen
	while i>0 and j>0:
		if strA[i-1] == strB[j-1]:
			finalStr.append(strA[i-1])
			i -= 1; j -= 1
		else:
			if table[i-1][j] > table[i][j-1]:
				i -= 1
			else:
				j -= 1
	finalStr.reverse()
	return "".join(finalStr)

def main():
	inputA = raw_input()
	inputB = raw_input()
	print longest_common_subsequence(inputA,inputB)

if __name__ == '__main__':
	main()