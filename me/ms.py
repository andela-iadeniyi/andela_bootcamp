#s = [5, 4, 7, 6, 11, 66]  
#f = [5, 4, 1, 7, 6, 11, 66]  
def find_missing(n, m):
  a = 0
  if len(n) == 0 and len(m) == 0:
    return 0
  elif len(n) < len(m):
    for i in m:
    	if i not in n:
    		a = i
    return a
  elif len(n) > len(m):
    for i in n:
    	if i not in m:
    		a = i
    return a
  for i in n:
    for j in m:
      if i == j:
        return 0