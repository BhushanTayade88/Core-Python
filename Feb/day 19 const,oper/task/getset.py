from student2 import *

print("----Statements----\n" \
      "1.Enter details--\n" \
      "2.display--\n" \
      "3.Exit--\n")
while True:
    
    ch=int(input("Enter Your choice----:"))
    if ch<=2:
        pass
            
    if ch==1:
        l=[]
        n=int(input("How many student details u want to insert  :"))

        for i in range(n):
            s=Student()
            a,b,c=int(input("Enter Student Rollno:")),input("Student name :"),int(input("Student  Marks:"))
            #l2=[a,b,c]
            s.setRollno(a)         #(int(input("enter Rollno  :")))
            s.setName(b)          #(input("enter Name  :"))
            s.setMarks(c)          #(int(input("enter Marks  :")))
            l.append(s)
            
    elif ch==2:
        for i in l:
            print("Srudent Rollno",i.getRollno())
            print("Student Name",i.getName())
            print(i.getMarks())
            
            
        
                               
    elif ch==3:
        break

    else:
        print("***Wrong Choice***")


