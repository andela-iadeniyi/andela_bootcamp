def data_type(n):
  if type(n) == str:
    return len(n)
  elif n == True or n == False:
    return n
  elif type(n) == int:
    if n < 100:
      return "less than 100"
    elif n > 100:
      return "more than 100"
    return "equal to 100"
  elif type(n) == list:
    if len(n) >= 3:
      return n[2]
    return None
  elif n == None:
    return "no value"
  else:
    return n