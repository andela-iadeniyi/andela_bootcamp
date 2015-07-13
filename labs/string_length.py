def string_length(n):
  li = []
  li1 = []
  a = 0
  lent = len(n)
  if type(n) == list:
    if lent == 1:
      li.append(len(n[0]))
      return li
    else:
      for i in n:
      	for j in i:
      		a += 1
      	li.append(a)
      	a = 0
      return li
  elif type(n) == dict:
    for i in sorted(n.items(),key=lambda x:x[0]):
      for j in i[1]:
      	a += 1
      li.append(a)
      a = 0
    return li1
  else:
    return [len(n)]