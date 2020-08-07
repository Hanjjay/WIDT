class HouseHan:
    lastname = "한"

    def __int__(self,name):
        self.fullname = self.lastname +name

    def travle(self,where):
        print("%s,%s 여행을 갔다."%(self.fullname,where))

    def love(self,other):
        print("%s,%s 사랑에 빠졋네"%(self.fullname,other.fullname))

    def fight(self,ohter):
        print("%s,%s 싸우네"%(self.fullname,other.fullname))

    def __add__(self,other):
        print("%s,%s 결혼했네"%(self.fullname,other.fullname))

    def __sub__(self,other):
        print("%s,%s 이혼했네"%(self.fullname,other.fullname))

class HouseKim(HouseHan):
    lastname = "김"
    def travle(self,where,day):
        print("%s,%s여행 %d일 가네."%(slef.fullname,other.fullname))


orajil = HouseHan("아내")
chumji = HouseKim("첨지")
orahjil.travel("부산")
chumji.travel("부산",3)
orajil.love(chumji)
orajil + chumji
orajil.fight(chumji)
orajil - chumji
