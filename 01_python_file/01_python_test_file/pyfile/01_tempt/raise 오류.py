class Bird:
    def fly(self):
        raise IndexError

class chicken:
    pass

kin=chicken
kin.fly()

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle=Eagle()
eagle.fly()
