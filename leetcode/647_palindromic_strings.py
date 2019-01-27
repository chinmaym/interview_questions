'''
 Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

# def countMore(usrString, i, j):
#     strLen = len(usrString)
#     count = 0
#     while i <strLen and j >=0:
#         if usrString[i] == usrString[j]:
#             count += 1
#         else:
#             break
#         i+=1
#         j-=1
#     return count
#
# def numPalindromes(usrString):
#     table = [[False for _ in range(len(usrString))] for _ in range(len(usrString))]
#     for i in range(len(usrString)):
#         for j in range(len(usrString)):
#             if usrString[i] == usrString[j]:
#                 table[i][j] = True
#     count = len(usrString)
#     # print count
#     for i in range(1, len(usrString)):
#         if usrString[i] == usrString[i-1]:
#             count += 1
#             count += countMore(usrString, i+1, i-2)
#     # print count
#     k = 1
#     while k <=len(usrString)/2:
#         for i in range(k, len(usrString)-k):
#             if table[i][i] == True:
#                 if table[i-k][i+k] == True and table[i+k][i-k] == True:
#                     count+=1
#                 else:
#                     table[i][i] = False
#         k+=1
#     return count

def countMore(usrString, i, j):
    strLen = len(usrString)
    count = 0
    while i <strLen and j >=0:
        if usrString[i] == usrString[j]:
            count += 1
        else:
            break
        i+=1
        j-=1
    return count

def numPalindromes(usrString):
    count = len(usrString)
    for i in range(1,len(usrString)):
        if usrString[i] == usrString[i-1]:
            count += 1
            count+= countMore(usrString, i+1, i-2)
    for i in range(1, len(usrString)):
        j = 1
        while i+j < len(usrString) and i-j >=0:
            if usrString[i+j] == usrString[i-j]:
                count += 1
            else:
                break
            j+=1
    return count

if __name__=="__main__":
    usrString = raw_input()
    print numPalindromes(usrString)
