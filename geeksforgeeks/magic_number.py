'''
A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5. 
First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5),...

Write a function to find the nth Magic number.

'''


def main():
	n = input()
	magicNum = 0
	product = 1
	while n:
		product = product*5
		if n&1:
			magicNum += product
		n>>=1
	return magicNum
if __name__=="__main__":
	print main()