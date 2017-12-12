'''
2 3 -2 4
output = 6
'''

def main():
	nums = map(int,raw_input().split())
	max_product_till_now = 1; min_product_till_now = 1; max_product = 1
	for i in nums:
		if i >0:
			max_product_till_now = max_product_till_now*i
			min_product_till_now = min(min_product_till_now*i,1)
		elif i == 0:
			max_product_till_now = min_product_till_now = 1
		else:
			temp = max_product_till_now
			max_product_till_now = max(min_product_till_now*i,1)
			min_product_till_now = temp*i
		if max_product < max_product_till_now:
			max_product = max_product_till_now

	return max_product
if __name__ == '__main__':
	print main()