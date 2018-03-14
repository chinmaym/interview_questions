'''
given infinite number of coins of denomination (25,10,5,1) find the number of ways.
'''


def getNumWays(totMoney,numWays = 0,memo={}):
    if totMoney == 0:
        return numWays
    if totMoney < 0:
        return 0
    if not memo.get(totMoney) is None:
        return  memo[totMoney]
    else:
        memo[totMoney] = getNumWays(totMoney-25,numWays+1,memo)+getNumWays(totMoney-10,numWays+1,memo)+\
        getNumWays(totMoney-5,numWays+1,memo)+getNumWays(totMoney-1,numWays+1,memo)
    return memo[totMoney]

def main():
    totMoney = 1
    print getNumWays(totMoney)


if __name__=="__main__":
    main()
