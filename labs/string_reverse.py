
def reverse_string(string):
  rev = ""
  if string is '':
    return None
  else:
    li = len(string)
    for i in range(li):
      rev += string[li-1]
      li -=1
    if rev == string:
      return True
  return rev
