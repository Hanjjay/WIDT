#재귀호출
def fac(n):
    if n <= 1 :
        return 1
    return n *fac(n-1)



print(fac(1))
print(fac(5))
print(fac(10))
