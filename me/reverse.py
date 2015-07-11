def reverse_string(string):
  rev = ""
  li = len(string)
  for i in range(li):
    rev += string[li-1]
    li -=1
  if rev == string:
    return "Palindrum"
  return rev
