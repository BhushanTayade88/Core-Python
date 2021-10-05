def Generator(x,y,z,op):
    if op == 1:
        while x < y :
            a = x
            yield a
            x += z
    else:
        while x > y :
            b = x 
            yield b
            x = x - z
            
op=int(input("Which Operation u want perpform **Press 1** for increment and **Press 2** for decrement  :"))
x=ord(input("Enter a star position of Alphabets  :"))
y=ord(input("Enter a End position of Alphabets  :"))
z=int(input("Enter a Increment no  :"))        
x=Generator(x,y,z,op)
if op == 1:
    for i in x:
        print(chr(i))
else:
    for i in x:
        print(chr(i))
