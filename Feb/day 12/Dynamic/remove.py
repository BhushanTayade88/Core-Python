'''
10.Remove completely the 5's from the list.
l = [1,5,6,7,5,2,7,8,5,9,5,4,5]
'''
l = [1,5,6,7,5,2,7,8,5,9,5,4,5]
print("List elements are  :",l)
n=int(input("which element u want t remove from list :"))

while n in l:
    l.remove(n)

print("fter removing ",n,"from list :",l)
