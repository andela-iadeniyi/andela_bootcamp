class PrimeChecker(object):
  #number = "number"
  
  def __init__(self, number=''):
    self.number = str(number)
  
  def is_prime(self):
    if len(self.number) != 0:
      	#con = int(self.number)
      	dec = '.'
      	for i in self.number.split():
      		if dec in i:
        		return False
      	else:
      		con = int(self.number)
      		i = 2
        	if con < 2:
          		return False
        	while i < con:
          		if con % i == 0:
					return False
          		else:
					i += 1
			return True
    else:
		return False

a = PrimeChecker(2)
print a.is_prime()