'''
4.Replace a word by another word in a file.
'''
f=open("testfile.txt","r")
a=f.read()
#print(a)
replace_word=a.replace("word","hello")
f.close()
f=open("testfile.txt","w")
f.write(replace_word)
f.close()
f=open("testfile.txt","r")
print(f.read())
f.close()
