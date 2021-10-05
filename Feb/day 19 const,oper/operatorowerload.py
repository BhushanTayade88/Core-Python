class A:
    def __init__(self,a):
        self.a=a
        
    def __str__(self):
        return f'answer={self.a}'
    def __add__(self,other):
        
        a = self.a + other.a
        
        #c = A(a)
        return A(a)
        #return self.a+other.a
    def __mul__(self,other):
        a = self.a * other.a
       
        #return self.a*other.a
        c = A(a)
        return c

a=A(100)
a1=A(200)
a2=A(50)
a5=A(60)
#c=a+a2+a5+a1
print(a+a1+a2)
'''
print(a*a1+a2)
print(a+a1)
print(a2+a1)
print(a2*a5)
30,40 a+a1
10,20 b +b1
'''
