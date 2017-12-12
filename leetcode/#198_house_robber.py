


def main():
	nums = map(int,raw_input().split())
	incl = 0; excl = 0
	for i in nums:
		new_excl = excl if excl > incl else incl
		incl = excl + i
		excl = new_excl
	return max(excl,incl)


if __name__ == '__main__':
	print main()