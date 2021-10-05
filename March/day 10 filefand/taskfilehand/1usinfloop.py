f=open("bhushan.txt","r")
##f.write('line1')
##f.write('\nline2')
##f.write('\nline3')
##f.write('\nline4')
##print("file is created")
##if f.readable():
##    
##for i in f.readline() :
##    print(i)
##        
while True:
    line=f.readline()
    if not line:
        break
    print(line)



#print(f.read())






##if f.readable():
##    #print(f.readlines())
##    
##    for i in f.readlines() :
##        print(i)
##        
###print(f.read())
f.close()
