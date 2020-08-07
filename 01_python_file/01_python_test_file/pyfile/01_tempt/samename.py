def find_smae_name(a):
  n = len(a)
  result =set()
  for i in range(0, n - 1):
    for j in range (i+1,n):
      if a[i]==a[j]:
        result.add(a[i])
  return result

name = ["Jay","Chanho","Sanho","Jay"]
print (find_smae_name(name))
name2 = ["Jay","Chanho","Sanho","Jay","Sanho"]
print (find_smae_name(name2))
