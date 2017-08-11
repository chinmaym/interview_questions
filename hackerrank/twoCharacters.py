
'''
input: beabeefeab
output: 5
'''
# MY SOLUTION TIME OUT DUE TO RECURSION
# def twoCharacterCheck(inputString):
# 	characterList = []
# 	prevChar = None
# 	for i in xrange(len(inputString)):
# 		currentChar = inputString[i]
# 		if inputString[i] not in characterList:
# 			characterList.append(currentChar)
# 			if len(characterList)>2:
# 				return False
# 		if currentChar == prevChar:
# 			return False
# 		prevChar = currentChar
# 	return True

# def reduceString(inputString):
# 	newStringList = []
# 	if inputString is None or len(inputString)<2:
# 		return []
# 	for i in xrange(len(inputString)):
# 		if twoCharacterCheck(inputString):
# 			return [inputString]
# 		newString = filter(lambda x:x!=inputString[i],inputString)
# 		newStringList.extend(reduceString(newString))
# 	return newStringList


# if __name__ == '__main__':
# 	inputLen = input()
# 	inputString = raw_input()
# 	ansList  = reduceString(inputString)
# 	maxlen=0
# 	for i in ansList:
# 		if len(i) > maxlen:
# 			maxlen = len(i)
# 	print maxlen

### THIS IS HOW TO DO IT  #####

if __name__=="__main__":
	inputLen = input()
	inputString = raw_input()
	ans =0
	for i in xrange(26):
		for j in xrange(26):
			if i==j:
				continue
			c1 = i
			c2 = j
			flag = 1
			l=0
			for c in inputString:
				if ord(c) - ord('a')!=c1 and ord(c) - ord('a')!=c2:
					continue
				if ord(c) - ord('a') == c1:
					l+=1
					c1,c2=c2,c1
				else:
					flag=0
					break
			if flag==1 and l>1:
				ans = max(ans,l)
	print ans

