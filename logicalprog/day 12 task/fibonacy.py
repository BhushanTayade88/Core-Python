'''
fibonacci series
'''
no = int(input("Enter a no  :"))
x,y = 0,1


for i in range(no):
     print(x)
     x,y = y,x+y
     
     
def fibo(n):
     x,y=0,1
     for i in range(n):
          print(x)
          x,y=y,x+y
fibo(no)
