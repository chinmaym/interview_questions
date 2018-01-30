'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 0
        if x<0:
            neg = 1
            x = -1*x
        xstr = str(x)
        revXstr = xstr[::-1]
        if ( -2147483648 <= int(revXstr) <=2147483647):
            if neg == 1:
                return -1*int(revXstr)
            else:
                return int(revXstr)
        else:
            return 0
