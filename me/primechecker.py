class PrimeChecker(object):
  number = "number"
  def __init__(self, number):
    self.number = number
    
  def is_prime(self):
    if self.number is '':
      return False
    else:
      if number > 1:
        for i in range(2,self.number):
          if (self.number % i) == 0:
            return False
          break
        else:
          return True
      else:
        return False