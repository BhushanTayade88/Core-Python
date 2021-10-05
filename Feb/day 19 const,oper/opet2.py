class A: 
    
    def __init__(self,a,b): 
        self.a=a 
        self.b=b 
  
    def  __str__(self):
        return f'addition of a is :{self.a}and b is {self.b}'
    
    def __add__(self, other): 
        a = self.a + other.a 
        b = self.b + other.b 
        
        return A(a,b)
       
  
i=A(10,20)
j=A(30,40)

print(i+j)


  
