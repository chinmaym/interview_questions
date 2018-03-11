'''
 Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
'''


def checkPalindrome(usrStr):
    j=strLen = len(usrStr)
    if strLen == 0:
        return True
    i = 0;j-=1
    usrStr = usrStr.lower()
    while i<strLen/2 and i<j:
        while not 97<=ord(usrStr[i])<=97+26:
            i += 1
        while not 97<=ord(usrStr[j])<=97+26:
            j -= 1
        if usrStr[i]!=usrStr[j]:
            return False
        i +=1;j-=1
    return True
def main():
    usrStr = "race a car"
    return checkPalindrome(usrStr)

if __name__=="__main__":
    print main()
