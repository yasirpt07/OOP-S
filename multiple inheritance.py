class Suzuki:
    alto = "Suzuki"

    def __init__(self, name):
        self.name = name

    def model(self):
        print("car model is", self.name)


class Bmw:
    M8 = "Bmw"

    def __init__(self, name):
        self.name = name

    def type(self):
        print("car type", self.name)


class Owner(Suzuki, Bmw):
    pass


OWNERS = Owner("Suzuki")
OWNERS.model()
OWNERS.type()
