'''
print("Start---A---File")
try:
    print("Strt Try block")
    
    print(10/2)
    print("End of try block")
except Exception as e:
    print("Except Block",e)
else:
    print("Else part ")

print("End ----A---File")

'''
print("Start---A---File")
try:
    print("Strt Try block")
    
    print(10/2)
    print("End of try block")
except :
    print("Except Block")
else:
    print("Else part ")

print("End ----A---File")
