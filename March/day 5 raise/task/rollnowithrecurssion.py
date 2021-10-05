class InvalidRollno(Exception):
    def __init__(self,msg):
        self.msg=msg

def m1(rolln):
    
            
    if rolln<0:
        
        raise InvalidRollno("Rollno should  be Positive no")
    elif rolln==0:
        raise InvalidRollno("Rollno should not be zero")
        
       
while True:        
    try:
        rn=int(input("Enter a rollno  :"))
        m1(rn)
        print("Student roll no is  :",rn)
        break
        
    except InvalidRollno as e :
        print(e)    

    except ValueError :
        print("Rollno should be Integer value")
    




    
