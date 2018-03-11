'''
merge sort program
'''


def merge(numList,l,m,h):
    arr1 = m-l+1
    arr2 = h-m
    a=[];b=[]
    for i in range(arr1):
        a.append(numList[l+i])
    for i in range(arr2):
        b.append(numList[m+1+i])
    i=0;j=0;k=l
    while i<arr1 and j<arr2:
        if a[i]<b[j]:
            numList[k] = a[i]
            i+=1
        else:
            numList[k] = b[j]
            j+=1
        k+=1
    while i<arr1:
        numList[k] = a[i]
        i+=1
        k+=1
    while j<arr2:
        numList[k] = b[j]
        j+=1
        k+=1


def mergeSort(numList,l,h):
    if l<h:
        mid = (l+h)/2
        mergeSort(numList,l,mid)
        mergeSort(numList,mid+1,h)
        merge(numList,l,mid,h)



if __name__=="__main__":
    numList = [20,90,30,10,80,60,40,50]
    mergeSort(numList,0,len(numList)-1)
    print numList
