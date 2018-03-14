'''
program to calculate possible number of steps to climb n steps
'''


def numOfWays(n,memo={}):
    if memo.get(n):
        return memo[n]
    if n==0:
        return 1
    if n<0:
        return 0
    memo[n] = numOfWays(n-1)+numOfWays(n-2)+numOfWays(n-3)
    return  memo[n]


def main():
    print numOfWays(5)
    print numOfWays(10)
    print numOfWays(37)


if __name__=="__main__":
    main()
