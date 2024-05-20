# higher order function
def addition(x, y): #passing function in a function
    return x+y


def square(a):
    return a*a
result = square(addition(2,4))

print(result)