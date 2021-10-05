'''
3.Count occurences of given word in a file.
'''
f=open("FileTask.txt","r")
a=f.read()
occur=a.count('word')
print(occur)
f.close()
