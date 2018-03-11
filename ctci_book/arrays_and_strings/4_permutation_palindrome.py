'''
program to check if any permutation of the string could be a palindrome
input : "Tact Coa"
output : True ("taco cat","atco cta")
'''

getLength = lambda s: sum([1 for i in s if i!=' '])


def check_permutation_palindrome(usrStr):
    counter = 0
    for i in usrStr:
        if i == ' ':
            continue
        if (counter & 1<<ord(i)-97) == 0:
            counter = counter | (1<<ord(i)-97)
        else:
            counter = counter & ~(1<<ord(i)-97)
    return (counter & (counter-1) == 0)

def main():
    usrStr = "tact coa"
    return check_permutation_palindrome(usrStr)

if __name__=="__main__":
    print main()
