'''
Given a string, we need to print all possible palindromes that can be generated using letters of that string.

Examples:

Input:  str = "aabcb"
Output: abcba bacab

nput:  str = "aabbcadad"
Output: aabdcdbaa aadbcbdaa abadcdaba
        abdacadba adabcbada adbacabda
        baadcdaab badacadab bdaacaadb
        daabcbaad dabacabad dbaacaabd
'''

def checkPalindrome(checkStr):
    strLen = len(checkStr)-1
    for i in xrange((strLen+1)/2):
        if checkStr[i] != checkStr[strLen-i]:
            return False
    return True
def getPalindromPermutations(inputStr,l,r,output):
    if l == r:
        if checkPalindrome(inputStr):
            output.add(''.join(list(inputStr)))
    else:
        for i in range(l,r+1):
            inputStr[i],inputStr[l] = inputStr[l],inputStr[i]
            getPalindromPermutations(inputStr,l+1,r,output)
            inputStr[i],inputStr[l] = inputStr[l],inputStr[i]
def main():
    userInput = raw_input()
    output = set()
    getPalindromPermutations(list(userInput),0,len(userInput)-1,output)
    return output
if __name__ == '__main__':
    print main()
