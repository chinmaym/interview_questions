'''
number array = [10, 21, 22, 100, 101, 200, 300]
output = 6
'''

def main():
	nums = [10, 21, 22, 100, 101, 200, 300]
	nums.sort()
	n=len(nums)
	count = 0
	for i in range(0,n-2):
		k = i+2
		for j in range(i+1,n-1):
			while k<n and nums[j] + nums[i] > nums[k]:
				k+=1
			count += k-j-1
	return count

if __name__ == '__main__':
	print main()