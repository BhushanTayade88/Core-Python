class AgeInvalideError(Exception):
    def __init__(self,msg):
        self.msg=msg

def m1(age):
    print("m1---")
    if age<0:
        raise AgeInvalideError("age Problem")
    print("m1----end")

try:
    m1(-6)

except AgeInvalideError as e :
    print("except block",e)

print("program end")
    
