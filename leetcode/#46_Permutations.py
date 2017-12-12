

#-----------------Top solution-------------------------
# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if not nums:
#             return []
#         length = len(nums)
#         if length == 1:
#             return [nums]
#         res = []
#         for pair in self.permute(nums[1:]):
#             for i in range(len(pair) + 1):
#                 newPair = pair[:i] + [nums[0]] + pair[i:]
#                 res.append(newPair)
#         return res


def permutate(nums,l,r,output):
	if l==r:
		output.append(list(nums))
	else:
		for i in range(l,r+1):
			nums[i],nums[l] = nums[l],nums[i]
			permutate(nums,l+1,r,output)
			nums[l],nums[i] = nums[i],nums[l]



if __name__=="__main__":
	nums = map(int,raw_input().split())
	output = []
	permutate(nums,0,len(nums)-1,output)
	print output