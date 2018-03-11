'''
program to find the k smallest element
'''
import random

def kSmallest(numList,l,h,k):
    pos = getPos(numList,l,h)
    if pos == k:
        return numList[pos]
    elif pos>k:
        return kSmallest(numList,l,pos-1,k)
    else:
        return kSmallest(numList,pos+1,h,k)


def getPos(numList,l,h):
    getRand(numList,l,h)
    val = numList[h]
    i=l
    for j in range(l,h):
        if numList[j] <= val:
            numList[j],numList[i] = numList[i],numList[j]
            i+=1
    numList[i],numList[h] = numList[h],numList[i]
    return i


def getRand(numList,l,h):
    randNum = random.randint(l,h)
    numList[randNum],numList[h] = numList[h],numList[randNum]


if __name__=="__main__":
    numList = [20,90,30,10,80,60,40,50]
    k=1
    print kSmallest(numList,0,len(numList)-1,len(numList)-1-k)
