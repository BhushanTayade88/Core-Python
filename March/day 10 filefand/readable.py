#f=open("test.txt","a")#------->writable returns True in(write["a"],append["a"],opperation such as Create["x"] modes)
f=open("test.txt","r")#------->readable returns only in only(reading mode["r"])
print("Is readable  :",f.readable())
print("Is writable  :",f.writable())
print("file Open  :")

if f.readable():
    print(f.read())
f.close()


