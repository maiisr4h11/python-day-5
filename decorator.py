#Decorators in Python : A decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

def my_decorator(func): #decorator
    def wrapper(): #wrapper
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()