def log_call(func):
    def wrapper(*args,**kwargs):
        print(f"calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result=func(*args,**kwargs)
        return result
    return wrapper
@log_call
def add(a,b):
    return a+b
@log_call
def subtract(a,b):
    return a-b
@log_call
def multiply(a,b):
    return a*b
@log_call
def greet():
    name=input("Enter your name:")
    print(f"hello {name}")
    
print(add(5, 3))
print(subtract(10, 4))
print(multiply(3, 7))
greet()