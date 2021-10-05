'''
7.l1 = ["Hello","Bye"]
  l2 = ["Pune","Mumbai"]

o/p :  ["Hello Pune","Hello Mumbai","Bye Pune","Bye Mumbai"] without using any built-in function.
###3do with list comprehention
'''
l1 = ["Hello","Bye"]
l2 = ["Pune","Mumbai"]
l3=[]
for i in l1:
    for j in l2:
        x=i+' '+j
        l3.append(x)
print(l3)
l4 = [x+' '+y for x in l1 for y in l2]
print(l4)
