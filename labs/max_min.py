
def mini(s):
  n = float('+inf')
  for num in s:
    if num < n:
      n = num
  return n
  
def maxi(n):
  if len(n) == 0:
    return 0
  maximum = n[0]
  for i in n:
    if i > maximum:
      maximum = i
  return maximum 
  
def find_max_min(n):
  if maxi(n) == mini(n):
    return [len(n)]
  return [mini(n), maxi(n)]