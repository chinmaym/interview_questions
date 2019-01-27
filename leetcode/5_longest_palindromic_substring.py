'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"

Asshole Input -
"321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"

'''


# def getLongestPalindromicSubstring(inputStr):
#     strLen = len(inputStr)
#     table = [[False for _ in xrange(strLen)] for _ in xrange(strLen)]
#     maxPalindromeLength = 1
#     start = 0
#     for i in xrange(strLen):
#         table[i][i] = True
#         if i < strLen-1 and inputStr[i] == inputStr[i+1]:
#             table[i][i+1] = True
#             start = i
#             maxPalindromeLength = 2
#     k = 3
#     while k<=strLen:
#         # print table
#         i=0
#         while i<strLen-k+1:
#             j = i+k-1
#             if inputStr[i] == inputStr[j] and table[i+1][j-1]:
#                 table[i][j] = True
#                 start = i
#                 maxPalindromeLength = k
#             i += 1
#         k+=1
#     return inputStr[start:start+maxPalindromeLength]

def getLongestPalindromicSubstring(s):
    start = 0
    maxLength = 1
    for i in range(len(s)):
        odd = s[i-maxLength-1:i+1]
        even = s[i-maxLength:i+1]
        print "odd ", odd, i-maxLength-1
        print "even ", even, i -maxLength
        if i-maxLength-1 >= 0 and odd == odd[::-1]:
            start = i-maxLength-1
            maxLength += 2
        if i-maxLength >= 0 and even == even[::-1]:
            start = i-maxLength
            maxLength += 1
    return s[start:start+maxLength]
def main():
    inputStr = raw_input()
    return getLongestPalindromicSubstring(inputStr)

if __name__=="__main__":
    print main()
