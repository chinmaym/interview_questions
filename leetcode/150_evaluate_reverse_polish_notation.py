'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

  Input = 2 1 + 3 *
  Output = 9
'''
import re

#--------------Best Solution---------------------------
def evaluateBest(userInput):
    stack = []
    ops = {'+': lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:int(float(x)/y)}
    for i in userInput:
        if i in ops:
            op = ops[i]
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(op(v1,v2))
        else:
            stack.append(int(i))
    return stack[-1]
'''

def evaluate(userInput):
    print userInput
    stack = list()
    result = 0
    for i in userInput:
        print stack
    	if re.match(r'^[+-]?[0-9]+',i):
    	    stack.append(eval(i))
        elif i == '+':
            if len(stack) < 2:
                raise Exception("Invalid instruction")
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 + val1
            stack.append(result)
        elif i == '/':
            if len(stack) < 2:
                raise Exception("Invalid instruction")
            val1 = stack.pop()
            val2 = stack.pop()
            result = int(float(val2) / val1)
            stack.append(result)
        elif i == '-':
            if len(stack) < 2:
                raise Exception("Invalid instruction")
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 - val1
            stack.append(result)
        elif i == '*':
            if len(stack) < 2:
                raise Exception("Invalid instruction")
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 * val1
            stack.append(result)
    return stack.pop()
'''


if __name__=="__main__":
    userInput = raw_input().split(' ')
    print evaluateBest(userInput)
