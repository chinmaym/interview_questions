"""
Left rotation of array by n.
"""

def rotatedArray(numArr, n):
    for i in range(n):
        temp = numArr.pop(0)
        numArr.append(temp)
    return numArr

if __name__=="__main__":
    numArr = map(int, raw_input().split())
    n = int(raw_input())
    print rotatedArray(numArr, n)
