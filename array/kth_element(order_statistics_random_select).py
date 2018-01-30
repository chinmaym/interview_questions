'''
Find the kth element using order statistics using random select.
'''

import random


def randomSelect(arr,l,h):
    p = random.randint(l,h)
    i = l-1
    arr[h],arr[p] = arr[p],arr[h]
    for j in xrange(l,h):
        if arr[j]<=arr[h]:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1
def findKthElement(arr,l,h,k):
    if l == h:
        return arr[l]
    if l<h:
        i = randomSelect(arr,l,h)
        if i == k:
            return arr[i]
        if k<i:
            return findKthElement(arr,l,i-1,k)
        else:
            return findKthElement(arr,i+1,h,k)



def main():
    # usrArr = [4,7,2,50,3000,1,-5]
    usrArr = map(int,raw_input().split())
    k = input()
    if k<0 or k>=len(usrArr):
        return "out of bounds"
    return findKthElement(usrArr,0,len(usrArr)-1,k-1)


if __name__=="__main__":
    print main()
