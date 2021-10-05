class Alphabets:
    def __init__(self,x,y,z,op):
        self.x = ord(x)
        self.y = ord(y)
        self.z = z
        self.op = op
    def __iter__(self):
        return self
    def __next__(self):
        if op == 1:
            if self.x<self.y:
                x = self.x
                self.x = self.x+self.z
                return x
            else:
                raise StopIteration()

        else:
            if self.x>self.y:
                x = self.x
                self.x = self.x-self.z
                return x
            else:
                raise StopIteration()
            


x=input("Enter start character of Alphabets  :")
y=input("Enter End character of Alphabets  :")
z=int(input("Enter a Increment or Decement no  :"))
op = int(input("Enter Which Operation u want perpform **Press 1** for increment and **Press 2** for decrement  :"))
a=Alphabets(x,y,z,op)

if op == 1:
    for i in a:
##        if i == :
        print(chr(i))
##        else:
##            print(chr(i))
else:
    for i in a:
        print(chr(i))
