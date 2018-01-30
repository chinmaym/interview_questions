'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

#--------------time complexity O(nlogn)----------------------------------
def getLongestCommonPrefix(strList):
    ret = ""
    strList.sort()
    longestCommonPrefix = strList[0]
    lastStr = strList[len(strList)-1]
    for i in xrange(len(longestCommonPrefix)):
        if i < len(lastStr) and longestCommonPrefix[i] == lastStr[i]:
            ret+=lastStr[i]
        else:
            return ret
    return ret


#----------time complexity O(n2)----------------
# def getLongestCommonPrefix(strList):
#     longestCommonPrefix = strList[0]
#     for i in xrange(1,len(strList)):
#         j=0
#         for j in xrange(len(strList[i])):
#             if j >= len(longestCommonPrefix):
#                 break
#             if strList[i][j] == longestCommonPrefix[j]:
#                 continue
#             else:
#                 longestCommonPrefix = longestCommonPrefix[0:j]
#                 break
#         if j < len(longestCommonPrefix):
#             longestCommonPrefix = strList[i]
#     return longestCommonPrefix

def main():
    strList = raw_input().split()
    if len(strList) == 0:
        return ""
    return getLongestCommonPrefix(strList)


if __name__=="__main__":
    print main()
