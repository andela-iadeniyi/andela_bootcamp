def fb(n, m):
	a = 0
	if len(n) < len(m):
		for i in m:
			for j in n:
				if i != j:
					a = i
		return a
	else:
		for i in n:
			for j in m:
				if i != j:
					a = i
		return a