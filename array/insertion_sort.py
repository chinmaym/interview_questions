'''

program to do insertion sort.
'''


def insertionSort(numList):
    i=1
    while i<len(numList):
        print numList[i],"----",numList
        j=i
        while numList[j]<numList[j-1] and j>0:
            temp = numList[j]
            numList[j] = numList[j-1]
            numList[j-1] = temp
            j-=1
        i+=1



if __name__=="__main__":
    numList = [20,90,30,10,80,60,40,50]
    insertionSort(numList)
    print numList
