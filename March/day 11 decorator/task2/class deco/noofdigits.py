#no of digits
num=int(input("Enter a no:"))
sum1=0
totaldig = 0
while num>0:
    rem = num % 10
    sum1 += rem
    num //= 10
    totaldig += 1
print("Som of the total digits are :",sum1)
print("Total Digits are :",totaldig)



