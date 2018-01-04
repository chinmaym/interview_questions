'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the
product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''

def getProductArray(nums):
    temp = 1
    prod = [1]*len(nums)
    for i,j in enumerate(nums):
        prod[i] = temp
        temp *= j
    temp = 1
    for i in range(len(nums)-1,-1,-1):
        prod[i] *= temp
        temp *= nums[i]
    return prod

def main():
    nums = map(int,raw_input().split())
    return getProductArray(nums)
if __name__=="__main__":
    print main()
