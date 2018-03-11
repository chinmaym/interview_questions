'''
program to return all subsets of a set
'''

#---------Recursive-------------------
def powerSetR(numList,memo=[]):
    if len(numList) == 0:
        if not numList in memo:
            memo.append(numList)
        return
    for i in range(len(numList)):
        subset = numList[:i]
        subset.extend(numList[i+1:])
        if not subset in memo:
            memo.append(subset)
        powerSet(subset,memo)
    if not numList in memo:
        memo.append(numList)

#-----------Iterative------------------

def powerSetI(numList,memo=[]):
    listLen = len(numList)
    for i in range(1<<listLen)


def main():
    numList = [1,2,3,4,5,6,7]
    memo = []
    powerSet(numList,memo)
    print len(memo),memo

if __name__=="__main__":
    main()
