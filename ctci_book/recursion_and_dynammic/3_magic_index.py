'''
program to find magic index in a sorted array.
'''




def findIndex(numList,l,h):
    if l>h:
        return -1
    mid = (l+h)/2
    if numList[mid] == mid:
        return mid
    if numList[mid]>mid:
        return findIndex(numList,l,mid-1)
    if numList[mid]<mid:
        return findIndex(numList,mid+1,h)


def main():
    numList = [-40,-30,1,3,5,8,9]
    print findIndex(numList,0,len(numList)-1)

if __name__=="__main__":
    main()
