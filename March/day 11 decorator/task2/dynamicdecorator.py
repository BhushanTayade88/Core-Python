def repeat(n):
    def call_printer(func):
        def inner(args):
            for i in range(n):
                print("*" * 15)
                func(args)
                print("*" * 15)
        return inner
    return call_printer
a=int(input("How many times u want repeat msg  :"))        
@repeat(a)
def printer(msg):
    print(msg)
    
msg=input("Enter a Message  :")
printer(msg)


