'''
Program to sort this array using quick sort.

'''

def partition(arr,l,h):
    i = l-1
    pivot = arr[h]
    for j in xrange(l,h):
        if arr[j]<=pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

def quickSort(arr,l,h):
    if l<h:
        p = partition(arr,l,h)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,h)


def main():
    userArr = [4,7,2,50,3000,1,-5]
    quickSort(userArr,0,len(userArr)-1)
    return userArr

if __name__=="__main__":
    print main()
