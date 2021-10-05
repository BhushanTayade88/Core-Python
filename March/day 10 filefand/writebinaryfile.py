f = open("emo.jpg","rb")
print("file opened")
copy=f.read()
f.close()
print("file is closedd")


print("file closed")
nf=open("emo2.jpg","wb")
print("new file open")

nf.write(copy)

nf.close()

print("new file is closed ")
