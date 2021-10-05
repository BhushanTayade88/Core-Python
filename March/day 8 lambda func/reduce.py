from functools import reduce
marks=[10,20,30,40,50,60,70,80,90,95]

total = reduce(lambda a,b:a+b,marks)
print(total)
