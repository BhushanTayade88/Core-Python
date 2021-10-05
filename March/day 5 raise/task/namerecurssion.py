class InvalidName(Exception):
    def __init__(self,msg):
        self.msg=msg

def m1(stname):
    if len(stname)>6:
        raise InvalidName("Name should be less than 6 char ")
    elif stname.isalpha()==False:
        raise InvalidName("you must have insert only aplphabets")
##    elif stname.isspace()==False:
##        raise InvalidName("No white spaces allowed in stname")
       
while True:        
    try:
        sn=input("Enter a  student name  :")
        m1(sn)
        print("Student name is  :",sn)
        break
        
    except InvalidName as e :
        print(e)    

##    except ValueError :
##        print("Rollno should be Integer value")
##    




    
