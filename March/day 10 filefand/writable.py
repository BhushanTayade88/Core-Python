##f=open("test2.txt","r")
##print("Is readable  :",f.readable())
##print("IS writable  :",f.writable())
##print(f.read())
##if f.writable():
##    f.write("bhushan")
##    print("data written")
##f.close()


f=open("test2.txt","a")
print("Is readable  :",f.readable())
print("IS writable  :",f.writable())
#print(f.read())
print("File open")
if f.readable():
    print(f.read())
if f.writable():
    f.write("bhushan")
    print("data written")
f.close()
