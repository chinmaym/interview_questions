
from datetime import datetime
def get_all(word):
	s = tuple(word)
	subsetList = []
	for i in range(1,len(s)+1):
		for z in range(len(s)+1-i):
			subsetList.append(word[z:z+i])
	return subsetList

def check(list1,list2):
	check_list = [0]*26
	check_list2 = [0]*26
	for i in list1:
		check_list[ord(i)-ord('a')]+=1
	for i in list2:
		check_list2[ord(i)-ord('a')]+=1
	for i in xrange(26):
		if check_list[i]!=check_list2[i]:
			return False
	return True

if __name__=="__main__":
	t = input()
	while t>0:
		t1=datetime.now()
		count = 0
		word = raw_input()
		for l in xrange(1,len(word)):
			for i in xrange(0,len(word)-l):
				i_word = word[i:i+l]
				for j in xrange(i+1,len(word)-l+1):
					j_word = word[j:j+l]
					if check(i_word,j_word):
						count+=1
		t2 = datetime.now()
		print count,(t2-t1).seconds
#		print count
		t-=1