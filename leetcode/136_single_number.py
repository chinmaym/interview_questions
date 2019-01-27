'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

def getUnique(numList):
    num = 0
    for i in numList:
        num ^= i
    return num

if __name__=="__main__":
    numList = map(int, raw_input().split())
    print getUnique(numList)
