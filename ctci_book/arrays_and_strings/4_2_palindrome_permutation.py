'''
program to check if permutation of the string is palindrome
input : "Tact Coa"
output : ["taco cat","atco cta"]
'''



def checkPermutation(usrStr):
    i = 0;j=len(usrStr)-1
    while i<=j:
        while usrStr[i] == ' ':
            i+=1
        while usrStr[j] == ' ':
            j -=1
        if usrStr[i] != usrStr[j]:
            return False
        i+=1;j-=1
    return True


def getPermutation(usrStr,l,r,permutatedList):
    if l==r:
        permutatedList.append(''.join(usrStr))
    else:
        for i in range(l,r+1):
            usrStr[i],usrStr[l] = usrStr[l],usrStr[i]
            getPermutation(usrStr,l+1,r,permutatedList)
            usrStr[i],usrStr[l] = usrStr[l],usrStr[i]

def main():
    usrStr = "tact coa"
    permutatedList = []
    getPermutation(list(usrStr),0,len(usrStr)-1,permutatedList)
    output = []
    for i in permutatedList:
        if checkPermutation(i):
            output.append(i)
    return output
if __name__ == "__main__":
    print main()
