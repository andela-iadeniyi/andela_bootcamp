def words(s):
	count = 0
	dico = {}
	d = s.split()
	li = []
	for j in d:
		if j.isdigit():
			li.append(int(j))
		else:
			li.append(j)

	for i in li:
		if i in dico:
			dico[i] = dico[i] + 1
		else:
			dico[i] = 1
	return dico