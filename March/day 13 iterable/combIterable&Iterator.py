class Myrange:
    def __init__(self,i,n,x):
        self.i = i
        self.n = n
        self.x = x
    
    def __iter__(self):
        return Increment(self.i,self.n,self.x) 
        #return Decrement(self.i,self.n,self.x) 
    
class Increment:
    def __init__(self,i,n,x):
        self.i = i
        self.n = n
        self.x = x
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.i<self.n:
            y = self.i
            self.i += self.x
            return y
        else:
            raise StopIteration()
     
class Decrement:
    def __init__(self,i,n,x):
        self.i = i
        self.n = n
        self.x = x
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i>self.n:
            y = self.i
            self.i = self.i - self.x
            return y
        else:
            raise StopIteration()
     

    
   
        
ope=int(input("Which Operation u want perpform **Press 1** for increment and **Press 2** for decrement  :"))


if ope == 1:
    x=int(input("Enter a star position no  :"))
    y=int(input("Enter a End position no  :"))
    z=int(input("Enter a Increment no  :"))
    a = Myrange(x,y,z)
    for i in a :
        print(i)
else:
    x=int(input("Enter a star position no  :"))
    y=int(input("Enter a End position no  :"))
    z=int(input("Enter a decrement no  :"))
    b = Myrange(x,y,z)
    for i in b:
        print(i)



