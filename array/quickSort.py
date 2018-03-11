'''

program to  quick sort a list
'''

def partition(numList,l,h):
    p = h
    i = 0;j=h-1
    while i<j:
        while i<=h and numList[i]<=numList[p]:
            i+=1
        while j>=l and numList[j]>numList[p]:
            j-=1
        if j>i:
            numList[i],numList[j] = numList[j],numList[i]
    numList[p],numList[j+1] = numList[j+1],numList[p]
    print numList
    return j+1

def quickSort(numList,l,h):
    if l<h:
        p = partition(numList,l,h)
        quickSort(numList,l,p-1)
        quickSort(numList,p+1,h)


if __name__=="__main__":
    numList = [20,90,30,10,80,60,40,50]
    quickSort(numList,0,len(numList)-1)
