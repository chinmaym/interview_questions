'''

check if all characters are unique in a string. No extra space

'''



def isUnique(usrStr):
    counter = 0
    for i in usrStr:
        if (1<<ord(i)-97 & counter) !=0:
            return False
        else:
            counter |= 1<<ord(i)-97
    return True

def main():
    usrStr = "aacvfg"
    return isUnique(usrStr)

if __name__=="__main__":
    print main()
