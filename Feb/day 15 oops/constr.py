class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return f'x={self.x},y={self.y}'

class B(A):
    def __init__(self,x,y):
        super().__init__(30,40)
        self.x=x
        self.y=y
        #super().__init__(30,40)
        
    def __str__(self):
        print(super().__str__())
        return f'x={self.x},y={self.y}'

b=B(10,20)
print(b)
