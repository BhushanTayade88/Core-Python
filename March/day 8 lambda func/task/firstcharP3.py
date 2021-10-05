'''
3.Program to find whether a given string starts with a given character using Lambda.
e.g If user enters string as 'Python' and character as P then it is true and if character is J then it is false
'''
l=['python','bhushan','rahul','kunal','tayade']

a=input("Enter a string   :")
char=list(map(lambda a:a[0] == 'p' ,a))
if char[0]== True:
    print("True")
else:
    print("False")
char2=lambda a:True if a[0] == 'p' else False 
print(char2('python'))
