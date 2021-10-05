'''
9.Program to copy alternative lines of one file to another.

odd and even 
'''
##f = open("bhushan.txt","r")
#a=f.readlines()

##f2=open("newtxt.txt","x")
##
##type(a)
##for i in range(0, len(a)):
##    if(i % 2 != 0):
##        f2.write(a[i])
##    else:
##        pass
## 
##f2.close()
## 
##f2 = open('newtxt.txt', 'r')
##
##print(f2.read())
## 
##f.close()
##f2.close()

##while True:
##    lines=f.readlines()
##    print(lines[0:len(lines):-1])
##    if not lines:
##        break
##    print(line)

##with open('bhushan.txt') as f1,open('newtxt.txt','w') as f2 :
##    while f1.readline():
##        f2.write(f1.readline())

with open('bhushan.txt') as f1,open('newtxt.txt','w') as f2 :
    data = f1.readlines()
    for i in range(len(data)):
        if i%2==0:
            f2.write(data[i])        
    
