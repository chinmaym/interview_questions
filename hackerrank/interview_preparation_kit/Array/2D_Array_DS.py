"""
hour glass problem.
Print the largest sum possible in 2D array.
INPUT
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
OUTPUT
19
"""


def getLargestSum(numArr):
    i = 0
    n = len(numArr)
    maxSum = 0
    while i<n-2:
        j=0
        while j<n-2:
            tempSum = numArr[i][j]+numArr[i][j+1]+numArr[i][j+2]+numArr[i+1][j+1]+numArr[i+2][j]+numArr[i+2][j+1]+numArr[i+2][j+2]
            if tempSum > maxSum:
                maxSum = tempSum
            j+=1
        i+=1
    return maxSum

if __name__=="__main__":
    numArr = []
    for i in range(6):
        numArr.append(map(int, raw_input().split()))
    print getLargestSum(numArr)
