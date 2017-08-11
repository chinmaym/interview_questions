
def stringReduce(origString):
	flag = 1
	while flag==1 :
		flag = 0
		newString = origString
		for i in xrange(len(origString)-1):
			if origString[i] == origString[i+1]:
				newString = origString[0:i]+origString[i+2:]
				flag=1
				break
		origString = newString
	return origString




if __name__=="__main__":
	origString = raw_input()
	print stringReduce(origString) or "Empty String"