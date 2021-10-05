l1=['bhushan','tayade','python']always wee should write string inside file

f=open('f1.txt','w')
for ele in l1:
    f.write(ele)#------->how to write in same line with white space betn words
#print(f.read())
f.close()
