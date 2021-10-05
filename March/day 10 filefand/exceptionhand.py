f=open("test.txt","at")
print("file is open")
try:
    f.read()
    f.write('bye')
    print("data written")
except:
    print("some issue")

finally:
    f.close()
    print("files closed")


