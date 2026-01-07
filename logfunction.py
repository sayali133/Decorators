#log every function call automatically
def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"calling {func.__name__}")
        result=func(*args,**kwargs)
        print(f"finished add{func.__name__}")
        return result
    return wrapper

@decorator
def add(a,b):
    return a+b
add(2,3)