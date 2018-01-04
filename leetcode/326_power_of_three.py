'''
 Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''


def main():
    n = input()
    if n>0 and 1162261467 % n == 0:
        return True
    else:
        return False
if __name__=="__main__":
    print main()
