"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
"""

def revWordString(s):
    i = j = k = 0
    while i < len(s):
        if s[i] == ' ' and s[i-1] != ' ':
            k = 0
            while k<(i-j)/2:
                s[j+k],s[i-k-1] = s[i-k-1],s[j+k]
                k+=1
        if s[i]!=' ' and s[i-1] == ' ':
            j = i
        i+=1
    i = 0
    while i <len(s)/2:
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        i+=1

    return ''.join(s[1:])



if __name__=="__main__":
    inputStr = raw_input()
    res = revWordString(list(inputStr+" "))
    print res, " - ", len(res) 
