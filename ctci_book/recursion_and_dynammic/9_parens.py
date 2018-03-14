'''
program to print all valid parens.
'''


def getValidParens(h,paren = '',l=1,parenList=[],count=0):
    if l>2*h:
        parenList.append(paren)
    else:
        if count >=0 and l+count<=2*h:
            getValidParens(h,paren+'(',l+1,parenList,count+1)
        if count>0:
            getValidParens(h,paren+')',l+1,parenList,count-1)
    return parenList

def main():
    parenCount = 4
    parenList = getValidParens(parenCount)
    print parenList

if __name__=="__main__":
    main()
