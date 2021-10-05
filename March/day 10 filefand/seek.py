f=open("test.txt",'r')
print("file open  ")
f.seek(28)
print(f.readline())


f.close()
print("file close")
       
