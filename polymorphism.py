class Animal:
    def sound(self):
        print("animal sound is")


class Lion(Animal):
    def sound(self):
        print("Roar")


class Dog(Animal):
    def sound(self):
        print("bark")


lion = Lion()
dog = Dog()
lion.sound()
dog.sound()
