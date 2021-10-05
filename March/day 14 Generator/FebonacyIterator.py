class Fibonacy:
    def __init__(self,n):
        self.x = 0
        self.y = 1
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.i<self.n:
            a = self.x
            self.x,self.y = self.y,self.x+self.y
            #self.y = self.x+self.y
            self.n = self.n-1
            return a
        else:
            raise StopIteration()
    

z=int(input("Enter a no for Fibonacy series  :"))
a=Fibonacy(z)
for i in a:
    print(i)

