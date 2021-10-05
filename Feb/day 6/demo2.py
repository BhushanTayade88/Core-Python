class A:
	pass

class B():
	pass

class C(object):
	pass

print(issubclass(A,object))

print(issubclass(B,object))

print(issubclass(C,object))