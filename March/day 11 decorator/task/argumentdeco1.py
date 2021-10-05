def decorator(*args, **kwargs):
    print("Inside decorator")
     
    def inner(func):
         
        print("Inside inner function")
        print("My name is ", kwargs['name']) 
         
        func()
         
       
    return inner
 
@decorator(name = "Bhushan")
def my_func():
    print("Inside actual function")
