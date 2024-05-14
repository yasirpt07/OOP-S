class Base:
    def __init__(self):
        self._a = "Vehicles"
        self.c = "Cars"


class Derived(Base):
    def __init__(self):

        Base.__init__(self)
        print(self._a)


obj1 = Base()
print(obj1._a)
print(obj1.c)
