def string_upper(func):
    def inner(args):
        x=args.upper()
        #print(x)
        func(x)
    return inner
def string_reverse(func):
    def inner(args):
        x=args
        a=x[::-1]
        func(a)
        #print(x.reverse())
    return inner

@string_upper
@string_reverse
def deco(msg):
    print(msg)
@string_upper
def deco2(msg):
    print(msg)

msg=input("Enter a string  :")
deco(msg)
deco2(msg)
