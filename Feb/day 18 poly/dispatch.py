'''
multiple dispatch
on cmd promt
pip install multipledispatch

and it is used for combining different data types
'''
from multipledispatch import dispatch


@dispatch(int,float)
def add(a,b):
    print(a+b)

add(10,20.5)

@dispatch(int,int)
def add(a,b):
    print(a+b)

add(10,32)
