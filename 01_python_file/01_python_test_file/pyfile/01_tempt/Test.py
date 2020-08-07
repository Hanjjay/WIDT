goal = 0
r= int(input("이자율을 입력해 주세요 :"))
a = int(input("매년초 적립할 금액을 입력해 주세요 :"))
n = int(input("몇년동안 적급할지 입력하여 주세요:"))

while True:
    if n == 0:
        break
    goal = goal + a*(1+r/100)**n
    n = n-1
    print(goal)
    

print(goal)
print("Jay")
