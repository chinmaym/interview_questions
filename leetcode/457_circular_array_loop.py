'''
You are given an array of positive and negative integers.
If a number n at an index is positive, then move forward n steps.
Conversely, if it's negative (-n), move backward n steps.
Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element.
Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop.
The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
'''

def checkLoop(numList):
    numListLen = len(numList)
    i = pos = hop = 0
    count = 1
    i = i+numList[i]
    while count < 2*numListLen:
        print i,pos
        if i<0:
            i = numListLen + i
        else:
            i = i%(numListLen)
        if pos == i:
            if hop == 1:
                return False
            return True
        if numList[pos] * numList[i] > 0:
            i += numList[i]
            hop += 1
        else:
            pos = i
            i = i+numList[i]
            hop = 1
        count += 1
    return False

if __name__=="__main__":
    numList = map(int, raw_input().split())
    print checkLoop(numList)
