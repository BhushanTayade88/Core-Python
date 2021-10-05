f=open("Uwords.txt","r")
a=f.read()
f2=open("newtestfile2.txt","w")
for i in a.split():
    if i.isupper():
        f2.writelines(i+"\n")
    else:
        pass

f2.close()
f2=open("newtestfile2.txt","r")
print(f2.read())

f.close()
f2.close()
