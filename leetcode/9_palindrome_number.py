'''
Determine whether an integer is a palindrome. Do this without extra space.
'''


def checkIfPalindrome(num):
    if num < 0:
        return False
    i = revnum = 0
    temp = num
    while temp!=0:
        revnum = revnum*10+temp%10
        temp /= 10
    if revnum == num:
        return True
    else:
        return False
def main():
    num = input()
    return checkIfPalindrome(num)

if __name__=="__main__":
    print main()
