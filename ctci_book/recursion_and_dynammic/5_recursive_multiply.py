'''
program to recursively multiply.
'''


def multiplyR(num1,num2,mul=0):
    if 1<<mul > num2:
        return 0
    if num2&(1<<mul):
        tot = num1<<mul
        return tot + multiplyR(num1,num2,mul+1)
    else:
        return multiplyR(num1,num2,mul+1)



def main():
    print multiplyR(3,9)

if __name__=="__main__":
    main()
