'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Time limit exceeded Input -
[4,-10,-11,-12,-8,-12,-14,-11,-6,2,-4,2,3,12,-3,-12,-14,-12,-8,-9,-6,-3,10,2,14,10,7,-7,-9,0,-9,10,-2,-5,14,5,-9,7,9,0,-14,12,10,4,9,-8,8,11,-5,-15,-13,-3,-11,4,14,11,-1,-2,
-11,5,14,-4,-8,-3,6,-9,9,12,6,3,-10,7,0,-15,-3,-13,-8,12,13,-5,12,-15,7,8,-4,-2,4,2,3,9,-8,2,-10,-1,6,3,-2,0,-7,11,-12,-2,3,-4,-2,7,-2,-3,4,-12,-1,1,10,13,-5,-9,-12,6,8,7,0,
7,-6,5,13,8,-14,-12]

'''

def getTriplet(numList):
    numList.sort()
    numListLength = len(numList)
    triplets = []
    i = 0
    j = numListLength-1
    while i<j:
        triplet = []
        triplet.extend([numList[i],numList[j]])
        k=i
        t=j
        while len(triplet) < 3:
            tripletSum = sum(triplet)
            # print triplet,k,t,tripletSum
            if tripletSum >= 0:
                if tripletSum > -1*numList[k]:
                    break
                k += 1
                if tripletSum + numList[k] == 0 and k<t:
                    triplet.append(numList[k])
            else:
                if tripletSum < -1*numList[k]:
                    break
                t -= 1
                if tripletSum + numList[t] == 0 and t>k:
                    triplet.append(numList[t])
            if numList[k]>0:
                break
            elif numList[t]<0:
                break
            elif not k<t:
                break
        if len(triplet)==3 and sum(triplet) == 0:
            triplet.sort()
            if triplet not in triplets:
                triplets.append(triplet)
            if abs(k-i)>(j-t):
                j-=1
            else:
                i+=1
        elif sum(triplet)<=0:
            i+=1
        elif sum(triplet)>0:
            j-=1
    return triplets

#---------------time complexity O(n3)-------------------------------
# def getTriplet(numList):
#     triplets = list()
#     for i in xrange(len(numList)-2):
#         for j in xrange(i+1,len(numList)-1):
#             for k in xrange(j+1,len(numList)):
#                 if numList[i]+numList[j]+numList[k] == 0:
#                     triplet = [numList[i],numList[j],numList[k]]
#                     triplet.sort()
#                     if triplet not in triplets:
#                         triplets.append(triplet)
#     return triplets
def main():
    numList = map(int,raw_input().split())
    if len(numList) < 3:
        return 0
    return getTriplet(numList)


if __name__=="__main__":
    print main()
