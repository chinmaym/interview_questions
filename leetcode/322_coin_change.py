'''
 You are given coins of different denominations and a total amount of money amount.
 Write a function to compute the fewest number of coins that you need to make up that amount.
 If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
'''

def getChange(coins,amount,memo={}):
    if amount<0:
        return -1
    if amount == 0:
        return 0
    if not memo.get(amount) is None:
        return memo[amount]
    memo[amount] = -1
    for i in coins:
        change = getChange(coins,amount-i,memo)
        if change!=-1 and memo[amount]==-1:
            memo[amount] = change+1
        elif change!=-1 and memo[amount]!=-1:
            memo[amount] = min(change+1,memo[amount])
    return memo[amount]


def main():
    coins = [2]
    amount = 1
    print getChange(coins,amount)


if __name__=="__main__":
    main()
