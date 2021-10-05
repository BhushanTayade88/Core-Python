class A:
    def __init__(self,a):
        self.a=a
       

    def __str__(self):
        return f'Answer is {self.a}'

    def __add__(self, other): 
        a = self.a + other.a 
        return A(a)
    def __sub__(self, other): 
        a = self.a - other.a 
        return A(a)
    def __mul__(self, other): 
        a = self.a * other.a 
        return A(a)
    def __truediv__(self, other): 
        a = self.a / other.a 
        return A(a)
    def __floordiv__(self, other): 
        a = self.a // other.a 
        return A(a)
    def __pow__(self, other): 
        a = self.a ** other.a 
        return A(a)
    def __mod__(self, other): 
        a = self.a % other.a 
        return A(a)
    
