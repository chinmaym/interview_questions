'''
Implementation of quick sort
'''


def getPivot(numList, s, l):
    p = s
    i = s+1
    j = l-1
    while i <= j:
        while i<l and numList[i] <= numList[p]:
            i += 1
        while j>s and numList[j] > numList[p]:
            j -= 1
        if i<j:
            numList[i], numList[j] = numList[j], numList[i]
    numList[p], numList[j] = numList[j], numList[p]
    return j


def quicksort(numList, s, l):
    if s < l:
        p = getPivot(numList, s, l)
        quicksort(numList, s, p-1)
        quicksort(numList, p+1, l)

if __name__=="__main__":
    numList = map(int,raw_input().split())
    quicksort(numList, 0, len(numList))
    print numList
