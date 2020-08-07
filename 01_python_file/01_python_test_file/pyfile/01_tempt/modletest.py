#모들

def sum(a,b):
    return a+b

#맥부의 경우 모들을 어떻게 사용해야 하는지 알지 못해서 타이핑으로만 대체하고 나머지는 책을 읽는다

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할수 없습니다.")
        return

    else:
        result = sum(a,b)
        return result


####

improt modle tset
print(modletest.safe_sum(3,4))

print(modeletest.safe_sum(3,'a'))



    
