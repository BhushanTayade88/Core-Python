
def m1(age):
    print("m1---")
    if age<0:
        raise ArithmeticError("age Problem")
    print("m1----end")

try:
    m1(-6)

except ArithmeticError as e :
    print("except block",e)

print("program end")
    
