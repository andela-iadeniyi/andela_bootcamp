def man(n):
	maxi = 0
	for i in n:
		if i < 0:
			if maxi <= 0:
				if maxi < i:
					maxi = i
				else:
					maxi = i
	return maxi
