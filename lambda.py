# # syntax
#  keyword = lambda
#  lambda arg:expression


# def addition(x, y):
#     return x+y
#
#
# print(addition(2, 5))


# a = lambda x, y: x + y
# print(a(2, 4))

# def func(a):
#     return lambda b: b + a
#
#
# x = func(3)
# print(x(5))


# Calculate the value of mathematical expression x*(x+89)^7 where
# x= 3 using lambda expression


m = lambda x: x * (x + 89) ** 7


print(m(3))
