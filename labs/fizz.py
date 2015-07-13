
def fizz_buzz(n):
  if n % 3 == 0:
    if n % 5 == 0:
      return "FizzBuzz"
    return "Fizz"
  elif n % 5 == 0:
     return  "Buzz"
  else:
    return n