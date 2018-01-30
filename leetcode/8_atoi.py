'''
Implement atoi to convert a string to an integer.
'''

def atoi(inputStr):
    val = 0
    integerLength = len(inputStr)
    if inputStr[0] == '-' and '0'<=inputStr[1]<='9':
        sign = -1
        start = 1
    elif inputStr[0] == '+' and '0'<=inputStr[1]<='9':
        sign = 1
        start = 1
    elif '0'<=inputStr[0]<='9':
        sign = 1
        start = 0
    else:
        return 0
    for i in xrange(start,integerLength):
        if not '0'<=inputStr[i]<='9':
            break
        val = val*10 + (ord(inputStr[i])-ord('0'))
    val = sign*val
    if val>2147483647:
        return 2147483647
    elif val<-2147483648:
        return -2147483648
    return val

def main():
    inputStr = raw_input().strip()
    if len(inputStr) == 0 or str in ['+','-','*','/']:
        return 0
    return atoi(inputStr)


if __name__=="__main__":
    print main()
