class A:

	def m(self):
		print("---m---")
		print(id(self))
		print(self.x)

a=A()
a.x=100

a1=A()
a1.x=200

print(a.x)
print(id(a))
print(a1.x)
print(id(a1))

a.m()
a1.m()
