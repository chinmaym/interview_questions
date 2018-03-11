'''
Input : "Mr John Smith"
Output : "Mr%20John%20Smith"
'''


def urlify(url):
    numSpaces = 0
    origLen = len(url)
    for i in url:
        if i ==' ':
            numSpaces += 1
    totLen = numSpaces * 3 - numSpaces + origLen
    for i in range(totLen):
        url.append(' ')
    j = origLen-1; i =totLen-1
    while i>=0:
        if url[j] == ' ':
            url[i] = '0'
            url[i-1] = '2'
            url[i-2] = '%'
            i -= 2
        else:
            url[i] = url[j]
        i-=1;j-=1
    return ''.join(url)

def main():
    url = "Mr John Smith"
    return urlify(list(url))

if __name__=="__main__":
    print main()
