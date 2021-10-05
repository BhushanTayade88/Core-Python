'''
10.Program to copy only uppercase alphabets in other file.
'''
f=open("testfile2.txt","r")
a=f.readlines()

f2=open("newtestfile1.txt","w")
for i in a:
    if i.isupper():
        f2.write(i)
    else:
        pass

f2.close()
f2=open("newtestfile1.txt","r")
print(f2.read())

f.close()
f2.close()
