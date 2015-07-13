def arith_geo(l):
  f = len(l)
  if f == 0:
    return 0
  if (l[1] - l[0] == l[2] - l[1]) and (l[3]- l[2] == l[2] - l[1]):
    return "Arithmetic"
  elif (l[1] / l[0] == l[2] / l[1]) and (l[3] / l[2] == l[2] / l[1]):
    return "Geometric"
  else:
    return -1