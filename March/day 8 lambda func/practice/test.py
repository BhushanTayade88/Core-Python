#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
r= lambda x:x+15
print(r(10))

m= lambda x,y:x*y
print(m(12,4))

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number

def multiply(n):
    return lambda x : x * n

result = multiply(2)
print("15 multiply by 2 is  :",result(15))

result = multiply(3)
print("15 multiply by 3 is  :",result(15))

#Write a Python program to sort a list of tuples using Lambda.

l=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
l.sort( key=lambda x:x[1] )
print(l)

#Write a Python program to sort a list of dictionaries using Lambda.
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':512, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sorted_models=sorted(models, key=lambda x : x['model'])
print("sorted models  :",sorted_models)


#odd even
l=[1,2,3,4,5,6,7,8,9]
l2=list(filter(lambda x:x%2 == 0 ,l))
print(l2)


#start with p or not
a=input("enter any string  :")
b=['bhushan','Python','parrot','kunal']
result=lambda x: True if x.startswith('p')or('P') else False 
print(result(a))
