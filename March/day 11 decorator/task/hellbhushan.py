def outer_func(func):
    def inner_func(*b):
        
            
            for i in b:
                print("Hello")
                func(i)
            
            
            
                print("How are you")
    return inner_func

@outer_func
def m1(a):
    print(a)
    
@outer_func
def m2(b):
    print(b)        
m1('mam')

m2("bhusahn","sachin",'chandra')
