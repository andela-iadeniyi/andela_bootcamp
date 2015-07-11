def fibo(n):	
	a, b = 1,1
	li = [0]
	while n > 1:
		li.append(a)
		a,b=b,a+b
		n -= 1
	return li

"""def fibo_sum(n, c=None):
	pass"""
