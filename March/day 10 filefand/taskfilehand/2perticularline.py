'''
2.Program to display particular line taken by user.
'''
f=open("bhushan.txt","r")

##print(f.tell())
##print(f.readline())
##print(f.tell())
##print(f.readline())
##print(f.tell())
##print(f.readline())
##print(f.tell())
##print(f.readline())


b=f.readlines()
print(b)
a=int(input("which line no u want see :"))
print(b[a-1])
##for i in range(len(b)):
##   
##    if i+1==a:
##        print(b[i])
##    
f.close()
