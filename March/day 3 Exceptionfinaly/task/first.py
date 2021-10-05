print("Program start")
try:
    print("Outer try start")
    a = 10/2
    try:
        print("Inner try start")
        b = [1,2,3]
        print(b[4])
        print("Inner try end")
    except  ValueError:
        print("Inner except block")

except ZeroDivisionError:
    print("outer except ValueError")

print("Program end")
