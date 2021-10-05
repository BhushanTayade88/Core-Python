num=int(input("Enter a no:"))
reverse=0
while num>0:
    rem = num % 10
    reverse = reverse * 10 + rem
    #0*10+5=5  5*10+4= 54
    #print(rem,end="")
    num //= 10
    
print(reverse)

