'''
multiple except block
'''

try:
    print("start try block")
    a=int(input("Enter a Value"))
    print(10/a)
    print("end try block ")

except (ValueError,ZeroDivisionError)as msg:
    print("plz Enter valid value",msg)

