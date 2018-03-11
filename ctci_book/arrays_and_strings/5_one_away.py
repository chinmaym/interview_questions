'''
To check if strings are one change away.
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False
'''


def check_one_away(str1,str2):
    charDict = {}
    count = 0
    count += abs(len(str1)-len(str2))

    for i in str1:
        if charDict.get(i) is None:
            charDict[i] = 0
        charDict[i] += 1
    for i in str2:
        if charDict.get(i) is None:
            count += 1
        else:
            charDict[i] -= 1
    for key,val in charDict.iteritems():
        count += val
    return count <=2

def main():
    str1 = "ple"
    str2 = "pale"
    return check_one_away(str1,str2)

if __name__=="__main__":
    print main()
