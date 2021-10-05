def repeat(n):
    def star(func):
        def inner(args):
            for i in range(n):
                print("*" * 30)
                func(args)
                print("*" * 30)
        return inner
    return star
        
@repeat(n=4)
def printer(msg):
    print(msg)
    
msg=input("Enter the message  :")
printer(msg)

#printer = repeat(4)printer)#star printer
#printer(msg)
