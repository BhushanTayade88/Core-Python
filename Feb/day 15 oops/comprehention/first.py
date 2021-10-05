'''
1.Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''
k = ['Ten', 'Twenty', 'Thirty']
v= [10, 20, 30]

d={}
d=dict(zip(k,v))
print(d)
d2={k[i]:v[i] for i in range(len(k))}
print(d2)
