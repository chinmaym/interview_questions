'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram
'''

def getAnagramsList(s,p):
    res = []
    pDict = dict()
    sDict = dict()
    for i in p:
        if pDict.get(i) is None:
            pDict[i] = 0
        pDict[i] +=1
    # print pDict
    for i in range(len(s)-len(p)+1):
        if check(s, dict(pDict), len(p), i):
            res.append(i)
    return res
def check(s, pDict, pLen, i):
    # print s[i:i+pLen]
    for j in s[i:i+pLen]:
        if pDict.get(j) is None or pDict.get(j) == 0:
            return False
        pDict[j] -= 1
    return True

if __name__=="__main__":
    s = raw_input()
    p = raw_input()
    print getAnagramsList(s,p)
