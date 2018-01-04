'''
Given an integer, write a function to determine if it is a power of two.
'''

def check_power_2(n):
    if n<1:
        return False
    return n&n-1 == 0

def main():
    n = input()
    print check_power_2(n)


if __name__ == '__main__':
    main()
