'''
Input: forgeeksskeegfor  Longest Palindrome: geeksskeeg
output:10
'''
def main(userString):
	strLength = len(userString)
	table = [[False for _ in range(len(userString))] for _ in range(len(userString))]
	for i in range(len(userString)):
		table[i][i] = True
	start = 0
	maxPalindromeLength = 1
	for i in range(strLength-1):
		if(userString[i]==userString[i+1]):
			table[i][i+1] = True
			start = i
			maxPalindromeLength = 2
	k=3
	while k<=strLength:
		i=0
		while i<strLength-k+1:
			j = i+k-1
			if table[i+1][j-1] and userString[i]==userString[j]:
				table[i][j] = True
				if k > maxPalindromeLength:
					start = i
					maxPalindromeLength = k
			i += 1
		k += 1
	return  start,maxPalindromeLength


if __name__=="__main__":
	userString = raw_input()
	i,l = main(userString)
	print userString[i:i+l]
