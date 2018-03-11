'''

Search an element in a sorted and rotated array


An element in a sorted array can be found in O(log n) time via binary search.
But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand.
So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time.
'''



def search(numList,l,h,k):
    mid = (l+h)/2

    if l>h:
        return -1
    if numList[mid] == k:
        return mid
    if k>=numList[l]:
        if k<numList[mid]:
            return search(numList,l,mid-1,k)
        else:
            return search(numList,mid+1,h,k)
    else:
        if k<numList[mid]:
            return search(numList,mid+1,h,k)
        else:
            return search(numList,l,mid-1,k)





if __name__=="__main__":
    numList = [3,4,5,1,2]
    print search(numList,0,len(numList)-1,3)
