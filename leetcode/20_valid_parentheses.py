'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


def main():
    userInput = raw_input()
    q = []
    for i in userInput:
        if i in ['[','{','(']:
            q.append(i)
        elif len(q) == 0:
                return False
        elif i == '}':
            if q.pop() != '{':
                return  False
        elif i ==']':
            if q.pop() != '[':
                return False
        elif i == ')':
            if q.pop() != '(':
                return False
    if len(q) > 0:
            return False
    return True
if __name__ == '__main__':
    print main()
