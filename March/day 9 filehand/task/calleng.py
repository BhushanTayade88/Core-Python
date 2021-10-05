from eng import *
print("----Statements-----\n" \
      "1.Enter Student Details according to streams--\n" \
      "2.Dispaly Engineering stream record--\n" \
      "3.Exit--\n")

while True:
    ch=int(input("Enter Your choice----:"))
    if ch<=2:
        pass
    if ch==1:
        d={}
        
        n=int(input("How many stream u want to insert  :"))
        for i in range(n):
            l=[]
            
            e=Engineering()
            a=input("Enter Stream  :")
            e.setStream(a)
            n=int(input("How many student record u want to insert in perticular stream :"))
            
            for i in range(n):
                s=Engineering()
                a,b,c=int(input("Enter Student Rollno:")),input("Student name :"),input("Student  Address:")
                s.setRollno(a)         
                s.setName(b)          
                s.setAddress(c)
                l.append(s)
            d[e]=l
    elif ch==2:
         while True:
             stream=input("which stream record u want to see  :")
             for stm,reco in d.items():
                 if stm.getStream()==stream:
                     print("Engineering Stream",stm.getStream())
                     for st in reco:
                         print("Srudent Rollno",st.getRollno())
                         print("Student Name",st.getName())
                         print("Student Address",st.getAddress())
                     break
                    
             else:
                 print("Sorry no record found  :")
             break          
    elif ch==3:
        break

    else:
        print("***Wrong Choice***")

