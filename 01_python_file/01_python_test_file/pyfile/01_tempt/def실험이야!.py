def sum(a,b):
    

    c = a+b
    return c

a = int(input("입력해줘!"))
b = int(input("이것도 입력해줘!"))
c= sum(a,b)


print(c)



def say():
    return 'HI'
d= say()
print(d)


def sum2(a,b):
    print("%d,%d의 합은 %d입니다"%(a,b,a+b))
sum2(3,4)
