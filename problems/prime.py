def is_prime(x):
	if x >= 2:
		for i in range(2, x):
			if i % i == 0:
				return False
			else:
  				return True
is_prime(4)