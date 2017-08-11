n,k = map(int,raw_input().split())

p = raw_input()

pl = [x for x in p]

l,r = 0,n-1
taken = set()
while l < r:
    if pl[l] != pl[r]:
        nw = max(pl[l],pl[r])
        taken.add(l)
        pl[l] = nw
        pl[r] = nw
        k -= 1
    l +=1
    r -=1


if k < 0:
    print -1

else:
    l,r = 0,n-1
    while l <= r:
        cst = 2
        if l in taken or l==r: cst = 1
        if cst <= k and pl[l] != "9":
            pl[l] = "9"
            pl[r] = "9"
            k -= cst
        l += 1
        r -= 1

    print "".join(pl)