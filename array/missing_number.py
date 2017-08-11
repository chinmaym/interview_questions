

if __name__=="__main__":
	t = input()
	while t:
		n = input()
		num_list = map(int,raw_input().split())
		total = 0
		for i in num_list:
			total +=i
		acc_tot = (n*(n+1))/2
		print acc_tot - total
		t-=1