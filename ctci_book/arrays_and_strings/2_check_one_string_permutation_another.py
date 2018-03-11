'''
check if one string is permutation of another.
'''



def checkPermutation(usrStr1,usrStr2):
    charDict = {}
    for i in usrStr1:
        if charDict.get(i) is None:
            charDict[i] = 0
        charDict[i] += 1
    for  i in usrStr2:
        if not charDict.get(i) is None:
            charDict[i] -= 1
    totSum = 0
    for key,val in charDict.iteritems():
        totSum += val
    if totSum != 0:
        return False
    else:
        return True

def main():
    usrStr1 = "asdfg   "
    usrStr2 = "gfdsa"
    return checkPermutation(usrStr1,usrStr2)

if __name__=="__main__":
    print main()
