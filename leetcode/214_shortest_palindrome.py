"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.
Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"
"""


def shortestPalindrome(s):
    rev = s[::-1]
    n = len(s)
    for i in range(n):
        # print rev[i:], " --- ", s[0:n-1-i]
        if rev[i:] == s[0:n-i]:
            # print i
            return rev[0:i]+s
    return s[:-1]+s


if __name__=="__main__":
    inputStr = raw_input()
    print shortestPalindrome(inputStr)
