'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

def getQ(dividend,divisor,l=0):
    m = (0+dividend)>>1
    if m*divisor == dividend:
        return m
    elif m*divisor<dividend:
        return getQ(dividend,divisor,m+1)
    else:
        return getQ(m-1,divisor,l)

def main():
    sign = 1
    return getQ(1,1)


if __name__=="__main__":
    print main()
