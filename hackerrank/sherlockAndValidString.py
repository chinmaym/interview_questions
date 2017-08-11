#!/bin/python

import sys,math

def isValid(s):
    change = 1
    freqList = [0]*26
    alphaTypes = 0
    count = 0
    for i in s:
        if not freqList[ord(i)-97]  == 0:
            alphaTypes+=1
        freqList[ord(i)-97]+=1
    for i in xrange(len(freqList)-1):
        if freqList[i] == 0:
            continue
        for j in xrange(i+1,len(freqList)):
            if i == j or freqList[j] == 0:
                continue
            if abs(freqList[i]-freqList[j]) < freqList[i]:
                count += abs(freqList[i]-freqList[j])
            else:
                count+=freqList[i]
    if count/(alphaTypes-1) or count == 0:
        return "YES"
    else:
        return "NO"

s = raw_input().strip()
result = isValid(s)
print(result)
