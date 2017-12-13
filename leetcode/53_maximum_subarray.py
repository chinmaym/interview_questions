'''
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6. 

Input : -2 1 -3 4 -1 2 1 -5 4
Output : 6
'''
def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        me=ms=nums[0]
        for x in nums[1:]:
            me=max(x,me+x)
            ms=max(me,ms)
        return ms

if __name__ == '__main__':
	nums = map(int,raw_input().split())
	print maxSubArray(nums)