num = 20

for i in range(num+1):
    if i>1:
        
        for j in range(2,i):
           if (i % j) == 0:
               #print(i,"is not a prime number")
               break
        else:
           print(i,"is a prime number")
           
    else:
        print(i,"is not prime no")

