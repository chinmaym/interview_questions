'''
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color.
Since answer can be large return it modulo 10^9 + 7.

Examples:

Input : n = 2 k = 4
Output : 16
We have 4 colors and 2 posts.
Ways when both posts have same color : 4
Ways when both posts have diff color :
4*(choices for 1st post) * 3(choices for
2nd post) = 12

Input : n = 3 k = 2
Output : 6
'''

def getNumberOfWays(n,k):
    total = diff = k
    same = 0
    for i in xrange(2,n+1):
        same = diff
        diff = total*(k-1)
        total = same + diff
    return total

def main():
    n,k = map(int,raw_input().split())
    return getNumberOfWays(n,k)

if __name__=="__main__":
    print main()
