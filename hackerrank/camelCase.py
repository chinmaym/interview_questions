

if __name__=="__main__":
	userString = raw_input()
	wordCount = 1
	for i in userString:
		if ord(i)>64 and ord(i)<92:
			wordCount+=1
	print wordCount