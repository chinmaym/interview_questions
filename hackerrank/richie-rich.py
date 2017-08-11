#!/bin/python

import sys,math

def richieRich(s, n, k):

    m=n-1
    l=0
    taken = set()
    while l<m:
        if s[l]!=s[m]:
            newPalin = max(s[l],s[m])
            taken.add(l)
            s[l] = s[m] = newPalin
            k-=1
        l+=1
        m-=1
    if k<0:
        return -1
    else:
        l =0
        m=n-1
        while l<=m:
            cst = 2
            if l in taken or l==m: cst = 1
            if cst<=k and s[l]!='9':
                s[l]=s[m] = '9'
                k-=cst
            l+=1
            m-=1
    return ''.join(s)

# with open('richie-rich-input.txt') as f:
#     q = f.readlines()
# n,k = map(int,q[0].split())
# s = q[1].strip()
n,k = map(int,raw_input().split())
s = raw_input().strip()
t = list(s)
result = richieRich(t, n, k)
print(result)
# with open('richie-rich-output.txt','w') as f:
#     f.write(result)