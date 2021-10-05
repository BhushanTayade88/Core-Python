def m1(*a,**b):
    print(a)
    print(b)
    for i in a:
        print(i)
    for k,v in b.items():
        print(k,"----->",v)
m1(10,20,30,a=20,b=14,c=15)
