'''
Input - 1 2 4 * +
Output - 9
Input - 5 2 ^
Output -  25
Input - 2 5 ^ 4 *
Output - 128
'''
def main():
	userExpression = raw_input()
	tokens = userExpression.split()
	stack = []
	while len(tokens) > 0:
		# print tokens , stack
		item = tokens.pop(0)
		if item.isdigit():
			stack.append(int(item))
		elif item == '+':
			stack.append(stack.pop()+stack.pop())
		elif item == '-':
			temp = stack.pop()
			stack.append(stack.pop()-temp)
		elif item == '*':
			stack.append(stack.pop()*stack.pop())
		elif item == '/':
			temp = stack.pop()
			stack.append(stack.pop()/temp)
		elif item == '^':
			temp = stack.pop()
			stack.append(stack.pop()**temp)
	return stack.pop()

if __name__=="__main__":
	print main()