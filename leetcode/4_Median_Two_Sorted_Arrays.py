'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

def getmedian(inputArr1,inputArr2,l1,l2,h1,h2):
    mid3 = ((len(inputArr1)+len(inputArr2))/2)-1
    while l1<=h1 and l2<=h2:
        mid1 = (l1+h1)/2
        mid2 = (l2+h2)/2
        m1 = inputArr1[mid1]
        m2 = inputArr2[mid2]
        if m1<m2:





def getMedian(inputArr1,inputArr2):
    arr1Length = len(inputArr1)
    arr2Length = len(inputArr2)
    mid1 = arr1Length/2
    mid2 = arr2Length/2
    mid3 = (arr1Length+arr2Length)/2



def main():
    # inputArr1 = map(int,raw_input().split())
    # inputArr2 = map(int,raw_input().split())
    inputArr1 = [1,3]
    inputArr2 = [2]
    return getMedian(inputArr1, inputArr2)



if __name__=="__main__":
    print main()
