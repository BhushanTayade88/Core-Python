class Myrange:
    def __init__(self,i,n,x,z):
        self.i = i
        self.n = n
        self.x = x
        self.z = z
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.z == 1:
            if self.i<self.n:
                y = self.i
                self.i += self.x
                return y
            else:
                raise StopIteration()
        else:
            if self.i>self.n:
                y = self.i
                self.i = self.i - self.x
                return y
            else:
                raise StopIteration()
        
ope=int(input("Which Operation u want perpform **Press 1** for increment and **Press 2** for decrement  :"))
x=int(input("Enter a star position no  :"))
y=int(input("Enter a End position no  :"))
z=int(input("Enter a Increment no  :"))
a=Myrange(x,y,z,ope)
if ope == 1:
    for i in a:
        print(i)
else:
    for i in a:
        print(i)
