


def getMaxSubarray(nums):
    minEndingHere = maxSoFar = maxEndingHere = None
    for i in nums:
        if i >0:
            if not maxEndingHere:
                maxEndingHere = i
                minEndingHere = 1
            else:
                maxEndingHere = maxEndingHere * i
                minEndingHere = min(minEndingHere * i,1)
        elif i == 0:
            if maxEndingHere <0:
                minEndingHere = maxEndingHere = 0
            else:
                minEndingHere = maxEndingHere = 1
        else:
            if not maxEndingHere:
                maxEndingHere = 1
                minEndingHere = i
            else:
                temp = maxEndingHere
                maxEndingHere = max(minEndingHere*i,1)
                minEndingHere = temp * i
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
    return maxSoFar

def main():
    nums = map(int,raw_input().split())
    return getMaxSubarray(nums)


if __name__ == '__main__':
    print main()
