'''
program to  solve tower of hanoi.
'''


def TOH(start,end,util,n):
    if n==1:
        end.append(start.pop())
    else:
        TOH(start,util,end,n-1)
        end.append(start.pop())
        TOH(util,end,start,n-1)

def main():
    start = [8,7,6,5,4,3,2,1]
    end = [];util = []
    TOH(start,end,util,len(start))
    print end

if __name__=="__main__":
    main()
