'''
5.Find longest words in a file.
e.g  I live in Pune city.

o/p:live
    Pune
    city
'''
f=open('pune.txt','r')
#print(f.read())
a=f.read()#-------->if we take readlines it genetrate error:list object has no attribute split
b=max(a.split(), key=len)
c=len(b)
l=[]
for i in a.split():
    if len(i)==c:
        l.append(i)

#print(b)
print(l)

f.close()

