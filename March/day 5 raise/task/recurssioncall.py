from student import *
class InvalidSrudDetails(Exception):
    def __init__(self,msg):
        self.msg=msg

print("----Statements-----\n" \
      "1.Enter Student Details--\n" \
      "2.Dispaly all Student Record--\n" \
      "3.Exit--\n")
def rollno(rn):       
    if rn<0:
        raise InvalidSrudDetails("Rollno should  be Positive no")
    elif rn==0:
        raise InvalidSrudDetails("Rollno should not be zero")
def stuname(stname):
    if len(stname)>6:
        raise InvalidSrudDetails("Name should be less than 6 char ")
    elif stname.isalpha()==False:
        raise InvalidSrudDetails("you must have insert only aplphabets")
def marks(mk):
    if mk<0:
        raise InvalidSrudDetails("Marks should be in positive no")
    
    elif mk>100:
        raise InvalidSrudDetails("Marks should not be greter than 100")
    
while True:
    ch=int(input("Enter Your choice----:"))
    if ch<=2:
        pass
    if ch==1:
        l=[]
        n=int(input("How many student details u want to insert  :"))
        for i in range(n):
            s=Student()
            
            while True:
                
                try:
                    
                    a=int(input("Enter Student Rollno:"))
                    rollno(a)
                    s.setRollno(a)
                    break
                    
                except InvalidSrudDetails as e :
                    print(e)    

                except ValueError :
                    print("Rollno should be Integer value")
            while True:        
                try:
                    b=input("Enter a  student name  :")
                    stuname(b)
                    s.setName(b)   
                    break
                    
                except InvalidSrudDetails as e :
                    print(e)

            while True:
                
                try:
                    c=int(input("Student  Marks:"))
                    marks(c)
                    s.setMarks(c)  
                    break
                    
                except InvalidSrudDetails as e :
                    print(e)    

                except ValueError :
                    print("Rollno should be Integer value")
                    
            l.append(s)

    elif ch==2:
        print("----Student record----\n" \
             "1.display all record--\n" \
             "2.perticular student record--\n" \
             "3.Exit--\n")
        while True:
            ch=int(input("Enter your choice  :"))
            if ch<=2:
                   pass
                   
            if ch==1:
                   for stu in l:
                       print("Srudent Rollno",stu.getRollno())
                       print("Student Name",stu.getName())
                       print("Student Marks",stu.getMarks())
                       
                 
            elif ch==2:
                   print("----Search record by----\n" \
                         "1.Rollno--\n" \
                         "2.Name--\n" \
                         "3.Exit--\n")

                   while True:
                       ch1=int(input("your choice :"))
                       if ch1<=2:
                           pass
                       if ch1==1:
                           srollno=int(input("Enter rollno  :"))
                           for st in l:           
                               
                               if st.getRollno()==srollno :
                                   
                                   print(" ***Record found*** ")
                                   print("Srudent Rollno",st.getRollno())
                                   print("Student Name",st.getName())
                                   print("Student Marks",st.getMarks())
                       
                                   break
                           else:
                               print("Sorry no record found")
                       elif ch1==2:
                           sname=input("Enter student name :")
                           for st in l:           
                               
                               if st.getName()==sname:
                                   
                                   print(" ***Record found*** ")
                                   print("Srudent Rollno",st.getRollno())
                                   print("Student Name",st.getName())
                                   print("Student Marks",st.getMarks())
                       
                                   break
                           else:
                               print("Sorry no record found")
                       elif ch1==3:
                           break
            
        
                               
    elif ch==3:
        break

    else:
        print("***Wrong Choice***")


