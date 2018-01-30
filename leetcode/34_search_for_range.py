'''
5 7 7 9 9 10
8
'''

def search_range(nums,target,l,h,f,numRange):
	# print l,h
	if l>h:
		return 0
	mid = (l+h)/2
	if f == 0:
		if nums[mid] >= target:
			if nums[mid] == target:
				if mid < numRange[0] or numRange[0] == -1:
					numRange[0] = mid
			search_range(nums,target,l,mid-1,f,numRange)
		else:
			search_range(nums,target,mid+1,h,f,numRange)
	else:
		if nums[mid] > target:
			search_range(nums,target,l,mid-1,f,numRange)
		else:
			if nums[mid] == target:
				if mid > numRange[1] or numRange[1] == -1:
					numRange[1] = mid
			search_range(nums,target,mid+1,h,f,numRange)
def main():
	nums = map(int,raw_input().split())
	target = input()
	numRange = [-1,-1]
	search_range(nums,target,0,len(nums)-1,0,numRange)
	search_range(nums,target,0,len(nums)-1,1,numRange)
	print numRange


if __name__ == '__main__':
	main()
