'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

#---------------------------------My Solution 2---------------------------------

def getzigzag(inputStr, rows):
    store = []
    j = 0
    r = 1
    for i in range(len(inputStr)):
        if len(store) < j+1:
            store.append("")
        store[j] += inputStr[i]
        j+=r
        if j == rows:
            r = -1
            j -= 2
        if j == -1:
            r = 1
            j += 2
    return ''.join(store)
#----------------------------------My Solution----------------------------------
# def getzigzag(inputStr,rows):
#     k = i = 0
#     j = 1
#     retStr = []
#     rowIndexDiff = [0 for _ in xrange(rows)]
#     for i in xrange(rows):
#         if i == 0 or i == rows-1:
#             rowIndexDiff[i] = (rows-2)*2+1+1
#         else:
#             rowIndexDiff[i] = (rows-2-(i))*2+1+1
#     print rowIndexDiff
#     for i in xrange(rows):
#         curIndex = i
#         diff1 = rowIndexDiff[i]
#         diff2 = rowIndexDiff[rows-1-i]
#         flag = 0
#         while curIndex < len(inputStr):
#             if flag == 0:
#                 retStr.append(inputStr[curIndex])
#                 curIndex += diff1
#                 flag = 1
#             else:
#                 retStr.append(inputStr[curIndex])
#                 curIndex += diff2
#                 flag = 0
#     return ''.join(retStr)


def main():
    inputStr = raw_input()
    rows = input()
    if rows == 1 or rows>=len(inputStr):
        return inputStr
    return  getzigzag(inputStr,rows)



if __name__=="__main__":
    print main()
