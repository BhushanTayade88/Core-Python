# Python code to illustrate 
# Decorators with parameters in Python 
 
def decorator_func(x, y):
 
    def Inner(func):
 
        def wrapper(*args, **kwargs):
            print("I like Python")
            print("Sum of values - {}".format(x+y) )
 
            func(*args,**kwargs)
             
        return wrapper
    return Inner
 
 
# Not using decorator 
def my_fun(*args):
    for ele in args:
        print(ele)
 
# another way of using dacorators
decorator_func(12, 15)(my_fun)('I', 'Like', 'Python')
