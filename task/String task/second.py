'''
2.Return the total count of string “Emma” appears in the given string without using count method and with using count method.

Given string: 
“Emma is good developer. Emma is a writer”

slicing 
'''
str1="Emma is good developer. Emma is a writer"
a=0
str2=str1.split(" ")
print(str2)
for i in str2:
    if i=='Emma':
        a=a+1
print("Emma appears",a,"times")
a=str1.count("Emma")
print("Emaa cames",a,"times")
        

    


    
