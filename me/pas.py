def num(n):
	dico = {}
	for i in n:
		a = 0
		for j in n:
			if i == j:
				a += 1
			else:
				a = 1
		dico[i] = a
	return dico