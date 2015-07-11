def find_missing(n, m):
  a = 0
  ss = set(n)
  fs = set(m)
  if len(n) == 0 and len(m) == 0:
    return 0
  elif len(n) < len(m) or len(n) > len(m):
    a = ss.union(fs)  - ss.intersection(fs)
  for i in n:
    for j in m:
      if i == j:
        return 0
    a = i
  return a