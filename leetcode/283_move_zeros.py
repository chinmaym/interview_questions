'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
'''


def moveZero(numList):
    i = j = 0
    while i <len(numList):
        while j<len(numList) and numList[j]!=0:
            j+=1
        if i>j and numList[i]!=0:
            numList[i],numList[j] = numList[j],numList[i]
        i+=1
    return numList


if __name__=="__main__":
    numList = map(int, raw_input().split())
    print moveZero(numList)
