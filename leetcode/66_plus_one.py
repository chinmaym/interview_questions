'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''

def addOne(nums):
    s = 0
    for i in xrange(len(nums)-1,-1,-1):
        s += nums[i]*pow(10,len(nums)-1-i)
    s +=1
    return [int(x) for x in str(s)]
def main():
    nums = map(int,raw_input().split())
    print addOne(nums)

if __name__ == '__main__':
    main()
