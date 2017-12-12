'''
Find sqrt of an integer. And if it's not a perfect square then return the floor of sqrt(x).
'''
import math
def binaryMethod(x):
	low = 0
	high = float(x)/2
	answer = None
	while low<=high:
		mid = (low+high)/2
		print low,high,mid
		foundSquare = mid*mid
		if foundSquare == x:
			return mid
		elif foundSquare > x:
			high = math.ceil(mid)-1
			answer = high
		else:
			low = math.floor(mid)+1
	return answer


def babylonianMethod(x):
	approxSquareRoot = float(x)/2
	diff = 0.01
	approxSquareRoot1 = (approxSquareRoot+x/approxSquareRoot)/2
	while abs(approxSquareRoot - approxSquareRoot1)>diff:
		print approxSquareRoot, approxSquareRoot1
		approxSquareRoot = approxSquareRoot1
		approxSquareRoot1 = (approxSquareRoot+x/approxSquareRoot)/2
	return approxSquareRoot1



def main():
	userInput = input("Enter an integer :")
	# squareRoot = babylonianMethod(userInput)
	squareRoot = binaryMethod(userInput)
	print "The square root of the integer is %d" %squareRoot

if __name__=="__main__":
	main()