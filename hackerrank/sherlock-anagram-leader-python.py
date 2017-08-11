from datetime import datetime

n=input()
for _ in xrange(n):
    time1 = datetime.now()
    s=list(raw_input())
    l=len(s)
    count=0
    for i in xrange(1,l):
        dic={}
        for j in xrange(l-i+1):
            t=str(sorted(s[j:j+i]))
            print t
            k=dic.setdefault(t,0)
            dic[t]+=1
            print dic
        for j in dic:
            print j,dic[j]
            count+=((dic[j])*(dic[j]-1))/2
            print count
    print count,(datetime.now()-time1).total_seconds()