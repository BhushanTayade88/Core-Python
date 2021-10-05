from studentmk import *
class StudentMarksValidation(Exception):
    def __init__(self,msg):
        self.msg=msg


print("----Statements-----\n" \
      "1.Enter Student Details--\n" \
      "2.Dispaly all Student Record--\n" \
      "3.Exit--\n")

def rollno(rn):
    if rn<0:
        raise StudentMarksValidation("Rollno should  be Positive no")
    elif rn==0:
        raise StudentMarksValidation("Roll no Always be greter than 0")

def stname(nm):
    if len(nm)>8:
        raise StudentMarksValidation("Name should be less than 8 char ")
    if nm.isalpha()==False:
        raise StudentMarksValidation("In Name no spetial character,No Blank space,No Empty field allowed")
def physics(ph):
    if ph<0:
        raise StudentMarksValidation("Marks should  be Positive no")
    elif ph>100:
        raise StudentMarksValidation("Marks must be less than or equal to 100")
def chemistry(ch):
    if ch<0:
        raise StudentMarksValidation("Marks should  be Positive no")
    elif ch>100:
        raise StudentMarksValidation("Marks must be less than or equal to 100")

def biology(bio):
    if bio<0:
        raise StudentMarksValidation("Marks should  be Positive no")
    elif bio>100:
        raise StudentMarksValidation("Marks must be less than or equal to 100")
def math(mt):
    if mt<0:
        raise StudentMarksValidation("Marks should  be Positive no")
    elif mt>100:
        raise StudentMarksValidation("Marks must be less than or equal to 100")
##def phyTopper(l):
##        phtopper=l.sort(key = lambda x: x[2]) 
##        return phtopper 

while True:
    ch = int(input("Enter Your choice  :"))
    if ch<=2:
        pass
    if ch==1:
        l=[]
        l2 = l.copy()
        n=int(input("How many student details u want to insert  :"))
        for i in range(n):
            s=Student()
            while True:
                try:
                    rn=int(input("Enter Roll no    :"))
                    rollno(rn)
                    s.setRollno(rn)
                    break
                except StudentMarksValidation as e:
                    print(e)
                except ValueError:
                    print("Roll no should be Integer value")
            while True:
                try:
                    nm=input("Enter student Name   :")
                    stname(nm)
                    s.setName(nm)
                    break
                except StudentMarksValidation as e:
                    print(e)
            while True:
                try:
                    ph=int(input("Enter physics marks  :"))
                    physics(ph)
                    s.setPhysics(ph)
                    break
                except StudentMarksValidation as e:
                    print(e)
                except ValueError:
                    print("Marks should be Integer value")
            while True:
                try:
                    ch=int(input("Enter Chemistry marks  :"))
                    chemistry(ch)
                    s.setChemistry(ch)
                    break
                except StudentMarksValidation as e:
                    print(e)
                except ValueError:
                    print("Marks should be Integer value")
            while True:
                try:
                    bio=int(input("Enter Biology marks  :"))
                    biology(bio)
                    s.setBiology(bio)
                    break
                except StudentMarksValidation as e:
                    print(e)
                except ValueError:
                    print("Marks should be Integer value")
            while True:
                try:
                    mt=int(input("Enter Math marks  :"))
                    physics(mt)
                    s.setMath(mt)
                    break
                except StudentMarksValidation as e:
                    print(e)
                except ValueError:
                    print("Marks should be Integer value")
            l.append(s)
            l2 = l.copy()
    elif ch==2:
        print("----Display data-----\n" \
              "1.Display all--\n" \
              "2.Display particular student with respect to parameter rollno or name--\n" \
              "3.Display toppers section--\n" \
              "4.Exit --\n")
        while True:
            ch=int(input("Enter your second choice for Display data :"))
            if ch<=2:
                   pass
            if ch==1:
                for stu in l:
                    print("Srudent Rollno",stu.getRollno())
                    a=stu.getName()
                    print("Student Name",a)
                    print(a,"Physics Marks",stu.getPhysics())
                    print(a,"Chemistry Marks",stu.getChemistry())
                    print(a," Biology Marks",stu.getBiology())
                    print(a,"Math Marks",stu.getMath())
                    
            elif ch==2:
                streco=input("Enter  studnt Rollno or Name:")
                try:
                    for st in l:
                        if st.getName()==streco:  
                            print(" ***Record found*** ")
                            print("Srudent Rollno",st.getRollno())
                            a=st.getName()
                            print("Student Name",a)
                            print(a,"Physics Marks",st.getPhysics())
                            print(a,"Chemistry Marks",st.getChemistry())
                            print(a," Biology Marks",st.getBiology())
                            print(a,"Math Marks",st.getMath())
##                        else:
##                            print("sorry no record found of :",streco)
                            
                except  ValueError:
                    for st in l:
                        if st.getRollno()==int(streco):  
                            print(" ***Record found*** ")
                            print("Srudent Rollno",st.getRollno())
                            a=st.getName()
                            print("Student Name",a)
                            print(a,"Physics Marks",st.getPhysics())
                            print(a,"Chemistry Marks",st.getChemistry())
                            print(a," Biology Marks",st.getBiology())
                            print(a,"Math Marks",st.getMath())
                        else:
                            print("sorry no record found of :",streco)
                        
                            
                    
##                    if st.getRollno()==streco :  
##                        print(" ***Record found*** ")
##                        print("Srudent Rollno",st.getRollno())
##                        a=st.getName()
##                        print("Student Name",a)
##                        print(a,"Physics Marks",st.getPhysics())
##                        print(a,"Chemistry Marks",st.getChemistry())
##                        print(a," Biology Marks",st.getBiology())
##                        print(a,"Math Marks",st.getMath())
##                        break
                       
                        
            elif ch==3:
                print("----Display toppers section-----\n" \
                      "1.Physics topper--\n" \
                      "2.Chemistry topper--\n" \
                      "3.Biology topper--\n" \
                      "4.Maths topper--\n" \
                      "5.Exit --\n")
                while True:
                    ch1=int(input("Enter no to see topper according to subject"))
                    if ch1<=4:
                        pass
                    if ch1==1:
                        print("Topper of Physics :")                      
                        l.sort( key=lambda l1:l1.getPhysics(), reverse=True)
                        maxl=l[0].getPhysics()
                        for stu in l:
                            if maxl == stu.getPhysics():
                                
                                print("Srudent Rollno",stu.getRollno())
                                b=stu.getName()
                                print("Student Name",b)
                                print(b,"Physics Marks",stu.getPhysics())
                            
                    elif ch1==2:
                        print("Topper of Chemistry :")
                        l.sort( key=lambda l1:l1.getChemistry(), reverse=True)
                        maxl=l[0].getChemistry()
                        for stu in l:
                            if maxl == stu.getChemistry():
                                
                                print("Srudent Rollno",stu.getRollno())
                                b=stu.getName()
                                print("Student Name",b)
                                print(b,"Physics Marks",stu.getChemistry())
                        
                    elif ch1==3:
                        print("Topper of Bology :")
                        l.sort( key=lambda l1:l1.getBiology(), reverse=True)
                        maxl=l[0].getBiology()
                        for stu in l:
                            if maxl == stu.getBiology():
                                
                                print("Srudent Rollno",stu.getRollno())
                                b=stu.getName()
                                print("Student Name",b)
                                print(b,"Biology Marks",stu.getBiology())
                    elif ch1==4:
                        print("Topper of Math :")
                        l.sort( key=lambda l1:l1.getMath(), reverse=True)
                        maxl=l[0].getMath()
                        for stu in l:
                            if maxl == stu.getMath():
                                
                                print("Srudent Rollno",stu.getRollno())
                                b=stu.getName()
                                print("Student Name",b)
                                print(b,"Math Marks",stu.getMath())
                    elif ch1==5:
                        break
                    else:
                        print("wrong choice")
                        
                        
                            
               
            
            elif ch==4:
                break
            else:
                print("wrong choice")
    elif ch==3:
        break
    else:
        print("you enter wrong no  :")




        
 
