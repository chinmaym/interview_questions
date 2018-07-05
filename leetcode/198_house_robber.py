


def main():
	nums = map(int,raw_input().split())
        prev = cur = 0
        for i in nums:
            temp = cur
            cur = max(cur,prev + i)
            prev = temp
        return cur

if __name__ == '__main__':
	print main()
