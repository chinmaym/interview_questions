'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3. Given word1 = "makes", word2 = "coding", return 1.

'''
def main():
	wordList = ["practice", "makes", "perfect", "coding", "makes"]
	word1 = "coding"
	word2 = "makes"
	ind1 = -1; ind2 = -1; minDist = float('inf')
	for indx,i in enumerate(wordList):
		if i == word1:
			ind1 = indx
		if i == word2:
			ind2 = indx
		if ind1 != -1 and ind2 != -1:
			minDist = min(minDist,abs(ind1-ind2))
	return minDist

if __name__ == '__main__':
	print main()