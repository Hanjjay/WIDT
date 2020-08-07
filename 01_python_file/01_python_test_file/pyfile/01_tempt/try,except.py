#try,except 사용

try:
    4/0

    3+2
except ZeroDivisionError as a:
    
    print(a)

#####


try:
    4/0
    3*4
except ZeroDivisionError:
    c= 3+4
    print(c)
    

#####
    
#try:
 #   4/0
  #  3*5
#except as b:
 #   print(b)

# as 에서 index 오류가 발생한다

#####


try:
    4/0
    3*4
except ZeroDivisionError:
    pass
print("pass")




####

    
