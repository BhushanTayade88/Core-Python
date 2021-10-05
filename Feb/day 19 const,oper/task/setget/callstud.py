from student3 import *
print("----Statements-----\n" \
      "1.Enter Student Details--\n" \
      "2.Dispaly all Student Record--\n" \
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
            s.setRollno(a)         
            s.setName(b)          
            s.setMarks(c)         
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
                               
                               if st.getRollno()==srollno:
                                   
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


