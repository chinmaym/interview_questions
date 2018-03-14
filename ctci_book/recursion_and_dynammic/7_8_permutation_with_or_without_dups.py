'''
permutation of a string which do not include duplication.
'''



def getPermutations(usrStr,l,h,permuteList=set()):
    if l>h:
        permuteList.add(''.join(usrStr))
    for i in range(l,h+1):
        usrStr[i],usrStr[l] = usrStr[l],usrStr[i]
        getPermutations(usrStr,l+1,h,permuteList)
        usrStr[i],usrStr[l] = usrStr[l],usrStr[i]
    return permuteList

def main():
    usrStr = "abc"
    print getPermutations(list(usrStr),0,len(usrStr)-1)

if __name__=="__main__":
    main()
