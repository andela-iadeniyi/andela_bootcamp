def max_negative(n):
	maxn = 0
	for i in n:
		if maxn > i and maxn <= 0:
			maxn = i
		else:
			maxn = i
	return maxn