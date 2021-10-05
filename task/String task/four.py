'''
4.String rotation program
Input: 
string = "pythonprogram"
d = 2

Output: 
Left Rotation:  thonprogrampy
Right Rotation:  ampythonprogr


'''
string = "pythonprogram"
print(string)
d=int(input("enter no for rotation   :"))
st1=string[0:d]
st2=string[d:]

st3=string[0:-d]
st4=string[-d:]


print("Left Rotation  :",st2+st1)
print("Right Rotation  :",st4+st3)
