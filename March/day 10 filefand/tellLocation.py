#f=open("test.txt","w")
f=open("test.txt","r")
print("Is readable  :",f.readable())
print("IS writable  :",f.writable())
#print(f.read())
print("File open")
if f.readable():
    #print(f.read())#dout what it is
    print(f.readline())#----->read line by line
    print(f.tell())#--------->gives the location of curssor
    #loc=f.tell()
    #print(loc)
    print(f.readline())
    print(f.tell())
    print(f.readline())
    print(f.tell())
    print(f.readline())
    print(f.tell())
    print(f.readline())

f.close()
