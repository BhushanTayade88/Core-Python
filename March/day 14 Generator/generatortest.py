
def even(x):
       while(x!=0):
           if x%2==0:
                 yield x
           x-=1
a=even(8)
for i in a:
     print(i)

     
##def func():
##       i=1
##       while i>0:
##                 yield i
##                 i-=1
##for i in func():
##             print(i)
