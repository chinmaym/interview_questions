'''
 All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''

def getRepeatedPatterns(s):
    if not s:
        return []
    r,p = set(), set()
    for i in xrange(len(s)-9):
        t = s[i:i+10]
        if t in p:
            r.add(t)
        else:
            p.add(t)
    return list(r)

def main():
    s = raw_input()
    return getRepeatedPatterns(s)


if __name__ == '__main__':
    print main()
