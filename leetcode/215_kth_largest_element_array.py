'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.
'''

import random



def getKthLargest(numList,l,h,k):
    pos = getposition(numList,l,h)
    print pos,k
    if pos == k:
        return numList[pos]
    if pos < k:
        return getKthLargest(numList,pos+1,h,k)
    else:
        return getKthLargest(numList,l,pos-1,k)


def getposition(numList,l,h):
    getrandPivot(numList,l,h)
    val = numList[h]
    ind = l
    for i in range(l,h):
        if numList[i] <= val:
            numList[ind],numList[i] = numList[i],numList[ind]
            ind += 1
    numList[ind],numList[h]  = numList[h],numList[ind]
    return ind

def getrandPivot(numList,l,h):
    randNum = random.randint(l,h)
    numList[h],numList[randNum] = numList[randNum],numList[h]

def main():
    numList = [3,2,1,5,6,4]
    k=2
    return getKthLargest(numList,0,len(numList)-1,len(numList)-1-(k-1))

if __name__=="__main__":
    print main()
