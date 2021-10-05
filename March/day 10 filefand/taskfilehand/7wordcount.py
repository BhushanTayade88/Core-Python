'''
7.Count no. of words in a file..
'''
f=open("testfile.txt","r")
a=f.read()
words=a.split()
print("no of words  :",len(words))
f.close()
