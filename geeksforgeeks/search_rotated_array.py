


class Solution(object):

	def search(self, nums, target):
		start = 0; end = len(nums)-1
		while start <= end:
			mid = (start+end)/2
			if nums[mid] == target:
				return mid
			if nums[low] <= target < nums[mid]:
				end = mid - 1
			elif nums[mid] > target:
				start = start + 1
			elif nums[mid] < target <= nums[end]:
				start = mid + 1
			else:
				end = end - 1
		return -1


if __name__=="__main__":
	numArray = [40, 50, 10, 20, 30]
	target = 10
	print Solution().search(numArray, target)
