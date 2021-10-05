try:
    print("start try block")
    print(10/0)
    print("end try block ")
except ZeroDivisionError:
    print("except block")
finally:
    print("finally --block")
print("end of program")


try:
    print("start try block")
    print(10/2)
    print("end try block ")
except ZeroDivisionError:
    print("except block")
finally:
    print("finally --block")
print("end of program")
