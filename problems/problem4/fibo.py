def fibo(n):
	a, b = 1,1
	li = [0]
	if type(n) == int:
		while n > 1:
			li.append(a)
			a,b=b,a+b
			n -= 1
	return li

def fibo_sum(n, i=None):
	init = 0
	final = n;
	li = []
	if i == "even":
		for i in fibo(n * n * n):
			if i % 2 == 0:
				init += i
				final -= 1
				li.append(init)
				init = i
			else:
				li.append(i)
			if final == 0:
				break
		return li
	elif i == "odd":
		for i in fibo(n * n * n):
			if i % 2 == 1:
				init += i
				final -= 1
				li.append(init)
				init = i
			else:
				li.append(i)
			if final == 0:
				break
		return li
	else:
		for i in fibo(n):
			init += i
		return init