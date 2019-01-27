"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
"""


def getSubArrays(numArr, target):
    count = 0
    subArrSum = 0
    freq = [0]*(len(numArr)+1)
    for i in range(len(numArr)):
        subArrSum += numArr[i]
        ind = subArrSum - target
        if ind>=0:
            count += freq[ind]
        freq[subArrSum] += 1
        if subArrSum == target:
            count += 1
    return count


#--------------BRUTE FORCE  O(n^2) -----------------------

# def getSubArrays(numArr, target):
#     count = 0
#     for i in range(len(numArr)):
#         arrSum = 0
#         for j in range(i, len(numArr)):
#             arrSum += numArr[j]
#             if arrSum == target:
#                 count += 1
#             if arrSum > target:
#                 break
#     return count

if __name__=="__main__":
    numArr = map(int, raw_input().split())
    target = input()
    print getSubArrays(numArr, target)
