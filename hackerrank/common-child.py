
if __name__=="__main__":

	s1 = raw_input()
	s2 = raw_input()
	dic = {}
	for i in range(len(s1)):
#		print i,dic
		if dic.get(s1[i]):
			dic[s1[i]].append(i)
		else:
			dic[s1[i]] = [i]
	taken = set()
	prev = -1
	maxCount=0
	count = 0

	for i in range(len(s2)):
		print s2[i:]
		prev = -1
		count = 0
		d1=dict(dic)
		for j1 in range(i,len(s2)):
			j=s2[j1]
			print j,d1,prev
			if j in d1.keys():
				print d1[j]
				for k in d1.get(j):					
					if k > prev:
						prev = k
						count+=1
						break
		if count > maxCount:
			maxCount = count
	print maxCount
