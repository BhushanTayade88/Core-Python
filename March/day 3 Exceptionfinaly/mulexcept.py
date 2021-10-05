'''
multiple except block
'''

try:
    print("start try block")
    a=int(input("Enter a Value"))
    print(10/a)
    print("end try block ")

except ValueError:
    print("plz Enter no")
except ZeroDivisionError:
    print("except block")
except:
    print("default---except")

