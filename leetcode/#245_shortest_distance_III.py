'''
same as #243 just that in this words can be same
'''

def main():
	wordList = ["practice", "makes", "perfect", "coding", "makes","practice"]
	word1 = "practice"
	word2 = "practice"
	ind1 = -1; ind2 = -1; minDist = float('inf')
	for indx,i in enumerate(wordList):
		if word1 == word2:
			if i == word1:
				if ind1 < ind2:
					ind1 = indx
				else:
					ind2 = indx
		else:
			if i == word1:
				ind1 = indx
			if i == word2:
				ind2 = indx
		if ind1 != -1 and ind2 != -1:
			minDist = min(minDist,abs(ind1-ind2))
	return minDist

if __name__ == '__main__':
	print main()