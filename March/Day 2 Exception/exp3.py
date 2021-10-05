print("Start---A---File")
try:
    print("Strt Try block")
    
    print(10/0)
    print("End of try block")
except Exception as e:
    print("Except Block",e)

print("End ----A---File")
