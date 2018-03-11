'''
program to do binary search
'''



def binarySearch(numList,l,h,key):
    mid = (l+h)/2
    if l>h:
        return -1
    if numList[mid] == key:
        return mid
    elif numList[mid] > key:
        h = mid -1
    else:
        l = mid + 1
    return binarySearch(numList,l,h,key)



if __name__=="__main__":
    numList = [10,20,30,40,50,60,70,80,90]
    print binarySearch(numList,0,len(numList)-1,90)
