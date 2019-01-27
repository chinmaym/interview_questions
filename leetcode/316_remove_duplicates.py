'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
Example 1:
Input: "bcabc"
Output: "abc"
Example 2:
Input: "cbacdcbc"
Output: "acdb"
Inputs:
cbaddabaa
'''

# def removeDuplicates(s):
#     charDict = {}
#     for i in range(len(s)):
#         charDict[s[i]] = i
#     sortedList = sorted(charDict.items(), key = lambda x: x[1])
#     m = 0
#     res = []
#     print charDict, sortedList
#     for i in sortedList:
#         c = i[1]
#         if charDict[i[0]] < m:
#             m = i[1]+1
#             print i[0], charDict, res, m
#             continue
#         for j in range(m,i[1]):
#             if s[j]<s[c] and charDict[s[j]] >= j:
#                 c = j
#         if c != i[1]:
#             res.append(s[c])
#             charDict[s[c]] = c
#         res.append(i[0])
#         m = i[1]+1
#         print i[0], charDict, res, m
#     return "".join(res)

def removeDuplicates(s):
    rindex = {c:i for i, c in enumerate(s)}
    result = ''
    print rindex
    for i, c in enumerate(s):
        print result,
        if c not in result:
            while c < result[-1:] and i < rindex[result[-1]]:
                result = result[:-1]
            result +=c
        print i,c, result
    return result


if __name__=="__main__":
    s = raw_input()
    print removeDuplicates(s)
