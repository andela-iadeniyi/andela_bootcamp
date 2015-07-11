def ap(l):
	a = 1
	d = l[0] - l[1]
	c = 0
	for i in l:
		if (a - i) == d:
			c = 1
		else:
			c = 0
		a = i
	if c == 1:
		return True
	return False
def gp(l):
	a = 1
	d = l[1] / l[0]
	c = 0
	for i in l:
		if (i / a) == d:
			c = 1
		else:
			c = 0
		a = i
	if c == 1:
		return True
	return False
def geo(l):
	if ap(l) == True and gp(l) == False:
		return "AP"
	elif ap(l) == False and gp(l) == True:
		return "GP"
	else:
		return "No"