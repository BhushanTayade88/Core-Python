#3.Program to count elements in a list without using built in function.

l1 = [0,2,4,6,3,8,9,0,'abc','sa','dsada','csd',10.5,11.2,2.3,5.5] 
  
total=0
charno = 0
floatno = 0
intno = 0

for num in l1: 
    # if num >= 0: 
    total += 1  
    if type(num)==str:
        charno += 1
    elif type(num)==float:
        floatno += 1
    elif type(num)==int:
        intno += 1
    
                 
print("Total Integers in the list: ", intno)
print("Total float value in the list: ", floatno)
print("Total string in the list: ", charno)
print("Total elements in the list: ", total)
