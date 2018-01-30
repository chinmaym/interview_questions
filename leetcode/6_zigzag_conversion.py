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

#------------------------------------Best Solution-----------------------------
  # def convert(self, s, numRows):
  #       """
  #       :type s: str
  #       :type numRows: int
  #       :rtype: str
  #       """
  #       """
  #       :type s: str
  #       :type numRows: int
  #       :rtype: str
  #       """
  #       if numRows == 1 or numRows >= len(s):
  #           return s
  #
  #       L = [''] * numRows
  #       index, step = 0, 1
  #
  #       for x in s:
  #           L[index] += x
  #           if index == 0:
  #               step = 1
  #           elif index == numRows -1:
  #               step = -1
  #           index += step
  #
  #       return ''.join(L)

#----------------------------------My Solution----------------------------------
def getzigzag(inputStr,rows):
    k = i = 0
    j = 1
    retStr = []
    rowIndexDiff = [0 for _ in xrange(rows)]
    for i in xrange(rows):
        if i == 0 or i == rows-1:
            rowIndexDiff[i] = (rows-2)*2+1+1
        else:
            rowIndexDiff[i] = (rows-2-(i))*2+1+1
    print rowIndexDiff
    for i in xrange(rows):
        curIndex = i
        diff1 = rowIndexDiff[i]
        diff2 = rowIndexDiff[rows-1-i]
        flag = 0
        while curIndex < len(inputStr):
            if flag == 0:
                retStr.append(inputStr[curIndex])
                curIndex += diff1
                flag = 1
            else:
                retStr.append(inputStr[curIndex])
                curIndex += diff2
                flag = 0
    return ''.join(retStr)


def main():
    inputStr = raw_input()
    rows = input()
    if rows == 1 or rows>=len(inputStr):
        return inputStr
    return  getzigzag(inputStr,rows)



if __name__=="__main__":
    print main()
