'''
8.Program to create a file where all letters of English alphabets are listed by specified no. of letters on each line.
e.g
if user enter 3 then,
ABC
DEF 
GHI
If user enter 4 then,
ABCD
EFGH
IJKL
'''

f=open("AtoZ.txt","r")
a=f.readline()
num=int(input("enter no for grouping according to u  :"))
with open("words1.txt", "w") as f:
    for i in range(0,len(a),num):
        words=a[i:i+num]+"\n"
        f.writelines(words)

f.close()
f=open("words1.txt","r")
print(f.read())
f.close
