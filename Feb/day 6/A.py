class A:
	def m1(self):
		print("m1.....")
		print(id(self))
		print(self.x)

a=A()
a.x=100

a1=A()
a1.x=200

print(a.x)
print(a1.x)
print(id(a))
print(id(a1))

a.m1()
a1.m1()
