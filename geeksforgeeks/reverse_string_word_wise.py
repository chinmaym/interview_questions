'''
Examples :

Input  : s = "geeks quiz practice code"
Output : s = "code practice quiz geeks"

Input  : s = "getting good at coding needs a lot of practice"
Output : s = "practice of lot a needs coding at good getting"
'''

def reverseWord(inputStr,start,end):
    strLen = end - start + 1
    for i in xrange(strLen/2):
        inputStr[start+i],inputStr[end-i] = inputStr[end-i],inputStr[start+i]


def reverseStr(inputStr):
    strLen = len(inputStr)
    temp = 0
    for i in xrange(strLen+1):
        if i == strLen or inputStr[i] == ' ':
            reverseWord( inputStr, temp, i-1)
            temp = i+1
        i += 1
    reverseWord(inputStr,0,strLen-1)
    return ''.join(inputStr)

def main():
    inputStr = list(raw_input())
    return reverseStr(inputStr)

if __name__=="__main__":
    print main()
