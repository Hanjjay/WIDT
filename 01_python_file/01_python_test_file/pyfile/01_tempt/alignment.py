def check(r,v):
  for i in range (0,len(r)):
    if v < r[i]:
      return i
  return len(r)

def Alignment(a):
  result = []
  while a:
    still = a.pop(0)
    checking = check(result,still)
    result.insert(checking,still)
  
  return result

list_a = [170,160,154,187,220,165,156,174,164,182,207]
print(list_a)
print(Alignment(list_a))
