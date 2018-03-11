'''
Given an array of integers. find the maximum XOR subarray value in given array. Expected time complexity O(n).

Examples:

Input: arr[] = {1, 2, 3, 4}
Output: 7
The subarray {3, 4} has maximum XOR value

Input: arr[] = {8, 1, 2, 12, 7, 6}
Output: 15
The subarray {1, 2, 12} has maximum XOR value

Input: arr[] = {4, 6}
Output: 6
The subarray {6} has maximum XOR value
'''



def getMaxSubarrayXOR(numList):
    maxXORNow = maxXOREnd = numList[0]
    for i in range(1,len(numList)):
        maxXorNow = maxXORNow ^ numList[i]
        maxXOREnd = max(maxXORNow,maxXOREnd)



if __name__=="__main__":
    numList = [1, 2, 3, 4]
