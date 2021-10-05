#f=open("test.txt","w")
f=open("test.txt","r")
print("Is readable  :",f.readable())
print("IS writable  :",f.writable())
#print(f.read())
print("File open")
if f.readable():
    print(f.read(3))#dout what it is
    
if f.writable():
    f.write('line1')
    f.write('\nLine2')
    f.write('\nLine3')
    f.write('\nLine4')
    f.write('\nLine5')
    print("data written")
f.close()
