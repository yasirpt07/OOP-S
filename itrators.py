# fruit = ("mango", "orange", "apple", "banana")
# x = iter(fruit)
# for i in x:
#     print(i)

class Inc_Num:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        if self.x < 20:
            n = self.x
            self.x = self.x + 1
            return n
        else:
            raise StopIteration


inc = Inc_Num()
obj = iter(inc)

for i in obj:
    print(i)
