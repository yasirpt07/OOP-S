# parent class
class Suzuki:
    alto = "Suzuki"

    def __init__(self, model):
        self.model = model

    def types(self):
        print("vehicle model", self.model)


# child class
class Components(Suzuki):

    def __init__(self, model, name):
        self.name = name
        self.model = model

    def accessories(self):
        print("component are", self.name)
        print("model are", self.model)


alto = Suzuki("alto")
alto.types()
object1 = Components("engine", "car")
object1.accessories()
