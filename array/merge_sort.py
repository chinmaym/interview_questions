'''
Program to sort using merge sort technique
'''

def merge(inputList,l,h):
    mid = (l+h)/2
    a = []
    b = []
    for i in xrange(l,mid+1):
        a.append(inputList[i])
    for i in xrange(mid+1,h+1):
        b.append(inputList[i])
    i = j = 0
    k = l
    while k<=h:
        if i<len(a) and j<len(b):
            if a[i]<=b[j]:
                inputList[k] = a[i]
                i += 1
                k += 1
            else:
                inputList[k] = b[j]
                j += 1
                k += 1
        elif j<len(b):
            inputList[k] = b[j]
            j += 1
            k += 1
        else:
            inputList[k] = a[i]
            i += 1
            k += 1

def mergeSort(inputList,l,h):
    if l<h:
        mid = (l+h)/2
        mergeSort(inputList,l,mid)
        mergeSort(inputList,mid+1,h)
        merge(inputList,l,h)


def main():
    userArr = [4,7,2,50,3000,1,-5]
    mergeSort(userArr,0,len(userArr)-1)
    return userArr

if __name__=="__main__":
    print main()
