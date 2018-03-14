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
    for i in range(1<<listLen):
        memo.append([numList[j] for j in range(listLen) if (i&1<<j)])


def main():
    numList = [1,2,3,4]
    memo = []
    powerSetI(numList,memo)
    print len(memo),memo

if __name__=="__main__":
    main()
