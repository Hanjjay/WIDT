#희문찾기 알고리즘 queue stack 사용
def finding(s):
  qu = []
  st = []
  for x in s :
    if x.isalpha():
      qu.append(x.lower())
      st.append(x.lower())
  
  while qu:
    if qu.pop(0) != st.pop():
      return False
  return True



print(finding("wow"))
print(finding("Madam, I'm Adam"))
print(finding("Hello"))
