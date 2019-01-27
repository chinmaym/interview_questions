import random
def randomPartition(arr, p, q):
    r = random.randint(p,q)
    print r
    arr[r], arr[q] = arr[q], arr[r]
    print arr
    i = p; j = q-1
    while i<j:
        while i<q and arr[i]<=arr[q]:
            i+=1;
        while j>=0 and arr[j]>arr[q]:
            j-=1;
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i]>arr[q]:
        arr[i], arr[q] = arr[q], arr[i]
        return i
    else:
        return q


def randomSelect(arr, p, q, k):
    print "-- ",arr," -- ",p," -- ",q, " -- ",k
    i = randomPartition(arr, p, q)
    print arr," || ",i
    if i == k:
        return arr[i]
    elif k<i:
        return randomSelect(arr,p,i-1,k)
    else:
        return randomSelect(arr,i+1,q,k)

if __name__=="__main__":
    arr = map(int, raw_input().split(','))
    k = int(raw_input())
    num = randomSelect(arr,0,len(arr)-1,len(arr)-k)
    print arr," ||| ", num
