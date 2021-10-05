'''
5.Given a dictionary, swap the key-value
d = {0:'a',1:'b',2:'c'}

Expected output:
{'a':0,'b':1,'c':2}
'''
d = {0:'a',1:'b',2:'c'}
d2={v:k for k,v in d.items()}
print(d2)
    
