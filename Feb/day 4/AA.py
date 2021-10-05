def m1(a,b):
	print("m1-----")
	z=a+b
	return z
print(__name__)
# if  __name__ == '__main__':
print("calling_____M1")
x= m1(40,50)
print(x)

print("again calling m1---")
y=m1(50,60)
print(y)
print("file----end")
