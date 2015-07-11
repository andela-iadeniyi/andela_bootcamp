
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
  li = []
  a = mini(n)
  b = maxi(n)
  li.append(a)
  li.append(b)
  return li