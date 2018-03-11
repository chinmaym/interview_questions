'''
 Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''


def getDistinct(numList):
    j=0;i=1
    while i <len(numList):
        while i<len(numList) and numList[i] != numList[j]:
            i+=1
        if i!=j+1:
            numList[j+1] = numList[i]
        i+=1;j+=1
    return numList[:j]



def main():
    numList = [1,1,2]
    return getDistinct(numList)

if __name__=="__main__":
    print main()
