class Toyota:
    def __init__(self, name):
        self.name = name

    def model(self):
        print("car model is", self.name)


class Bmw(Toyota):
    def __init__(self, name):
        self.name = name

    def type(self):
        print("car type", self.name)


class Owner(Bmw):
    pass


OWNERS = Owner("Suzuki")
OWNERS.model()
OWNERS.type()
