'''
string compression
aabccccaaa -> a2b1c4a3
'''


def compressed(usrStr):
    retStr = []
    count = 1
    for i in range(len(usrStr)-1):
        if usrStr[i]!=usrStr[i+1]:
            retStr.append(usrStr[i]+str(count))
            count = 1
        else:
            count +=1
    retStr.append(usrStr[i]+str(count))
    if len(retStr)<len(usrStr):
        return ''.join(retStr)
    else:
        return usrStr

def main():
    usrStr = "aabccccaaa"
    return compressed(usrStr)

if __name__=="__main__":
    print main()
