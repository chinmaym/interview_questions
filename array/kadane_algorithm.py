

if __name__=="__main__":
	num_list = map(int,raw_input().split())
	max_till_now = max_now = num_list[0]
	for i in num_list[1:]:
		max_till_now = max(i,max_till_now+i)
		max_now = max(max_now,max_till_now)
	print max_now
