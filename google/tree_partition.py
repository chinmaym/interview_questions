'''
You're given a list of trees where each number corresponds to the type of fruit it has.
Eg. [1, 2, 1, 3, 4, 3, 5, 1, 2] has 5 types of fruits on that row of trees.
Some random female (root of all problems I swear) has 2 baskets and wants to fill each basket with only 1 type of fruit (Basically she wants to pick only 2 types of fruits).
She can start walking from any point and stops when she encounters a 3rd type of fruit. So in this example, max is 3 (either 1,2,1 or 3,4,3). Find max number of fruits she can pick
'''

def getMaxFruits(numList):
    fruit1 = fruit2 = count = maxFruit = 0
    for i in range(len(numList)):
        if fruitDict.get(numList(i)) is None:
            if len(fruitDict) == 2:
                if fruitDict[fruit1] + fruitDict[fruit2] > maxFruit:
                    maxFruit = fruitDict[fruit1] + fruitDict[fruit2]
                if fruit1 == numList[i-1]:
                    fruitDict.pop(fruit2)
                else:
                    fruitDict.pop(fruit1)
                    fruit1 = fruit2
            else:
                fruitDict[numList[i]]



if __name__ == "__main__":
    numList = map(int, raw_input().split())
    print getMaxFruits(numList)
