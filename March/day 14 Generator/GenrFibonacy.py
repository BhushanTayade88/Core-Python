
def fibonacy(n):
    x = 0
    y = 1
    while n > 0:
        yield x
        x,y = y,x+y
        n=n-1
        
no = int(input("Enter a no  :"))
x = fibonacy(no)
for i in x:
    print(i)
