'''
Maximum Product Subarray

Given an array that contains both positive and negative integers,
find the product of the maximum product subarray. Expected Time complexity is O(n) and only O(1) extra space can be used.

Examples:

Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -3, 0, -2, -40}
Output:   80  // The subarray is {-2, -40}

'''

def getMaxSubarray(nums):
    minEndingHere = maxSoFar = maxEndingHere = 1
    for i in nums:
        if i >0:
            maxEndingHere = maxEndingHere*i
            minEndingHere = min(minEndingHere*i,1)
        elif i == 0:
            maxEndingHere = 1
            minEndingHere = 1
        else:
            temp = maxEndingHere
            maxEndingHere = max(minEndingHere*i,1)
            minEndingHere = temp * i
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
    return maxSoFar

def main():
    nums = map(int,raw_input().split())
    return getMaxSubarray(nums)


if __name__ == '__main__':
    print main()
