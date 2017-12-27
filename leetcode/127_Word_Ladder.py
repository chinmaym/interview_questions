




def findDiff(str1,str2):
    diff = 0
    for i in enumerate(str1):
	diff += ord(str1(i))-ord(str2(i))
    return diff

if __name__=="__main__":
    beginWord = raw_input()
    endWord = raw_input()
    wordList = raw_input().split(' ')
    if endWord not in wordList:
	return 0
    diffDict = dict()
    for i in wordList:
        diff = 
