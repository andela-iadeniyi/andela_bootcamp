def ms():
	n = {'t': 'This', 'i': 'is', 'a': 'Andela'}
	li = []
	li1 = []
	a = 0
	for i in sorted(n.items(),key=lambda x:x[0]):
		for j in i[0]:
			li.append(a)
			a += 1
		a = 0
	for k in li:
		if li[k] > li[k + 1]:
			li1.append(k)
		li1.append(k)
	return li1