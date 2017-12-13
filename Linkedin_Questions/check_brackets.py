import Queue

def main(userInput):
	q=[]
	for i in range(len(userInput)):
		print q
		if userInput[i] in ['(','{','[']:
			q.append(userInput[i])
		elif userInput[i] == ')':
			if q.pop() == '(':
				continue
			else:
				return False
		elif userInput[i] == '}':
			if q.pop() == '{':
				continue
			else:
				return False
		elif userInput[i] == ']':
			if q.pop() == '[':
				continue
			else:
				return False
	if len(q)>0:
		return False
	return True


if __name__=="__main__":
	userInput = raw_input()
	print main(userInput)
