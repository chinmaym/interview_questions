'''
Given an array of strings (all lowercase letters),
the task is to group them in such a way that all strings in a group are shifted versions of each other.
Two string S and T are called shifted if,
Input  : str[] = {"acd", "dfg", "wyz", "yab", "mop",
                 "bdfh", "a", "x", "moqs"};

Output : a x
         acd dfg wyz yab mop
         bdfh moqs
All shifted strings are grouped together.
'''

def getDiff(a,b):
    diff1 = abs(ord(a)-ord(b))
    diff2 = 26 - diff1
    return str(diff1) if diff1<diff2 else str(diff2)

def getGroups(strList):
    diffDict = {}
    for i in strList:
        diff = ''
        for j in xrange(len(i)-1):
            diff += getDiff(i[j],i[j+1])
        if diffDict.get(diff) is None:
            diffDict[diff] = list()
        diffDict[diff].append(i)
    return diffDict.values()
def main():
    strList = ["acd","dfg","wyz","yab","mop","bdfh","a","x","moqs"]
    return getGroups(strList)


if __name__ == '__main__':
    print main()
