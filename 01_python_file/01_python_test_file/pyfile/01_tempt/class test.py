class service:
    check = (" perpect working")
    def __init__(self,name):
        self.name = name
    def sum (self,a,b):
        result = a+b
        print("%s님 %s+%s=%s 입니다."%(self.name,a,b,result))


jay = service("한재이")
jay.sum(63,12)
