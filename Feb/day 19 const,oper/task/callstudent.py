from student import *

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
            s=Student(int(input("Enter Student Rollno:")),input("Student name :"),int(input("Student  Marks:")))
            l.append(s)
    elif ch==2:
                
        print("----Student record----\n" \
             "1.display all record--\n" \
             "2.perticular student record--\n" \
             "3.Exit--\n")
        while True:
            ch=int(input("enter your choice  :"))
            if ch<=2:
                   pass
                   #sname=input("enter name")
            if ch==1:
                   for stu in l:
                       print(stu)
                   
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
                           srollno=int(input("enter rollno  :"))
                           for st in l:           
                               
                               if st.sturollno==srollno:
                                   
                                   print("record found ",st)
                                   break
                           else:
                               print("no record found")
                       elif ch1==2:
                           sname=input("Enter student name :")
                           for st in l:           
                               
                               if st.stuname==sname:
                                   
                                   print("record found ",st)
                                   break
                           else:
                               print("no record found")
                       elif ch1==3:
                           break
            elif ch==3:
                break  
    elif ch==3:
        break

    else:
        print("***Wrong Choice***")


