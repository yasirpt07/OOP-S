def my_decorator(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper()


@my_decorator
def add():
    return 5+2


print(add)
