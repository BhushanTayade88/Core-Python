class employee:
       
        def __init__(self,id,name,desg,sal,city):
                self.id=id
                self.name=name
                self.desg=desg
                self.sal=sal
                self.city=city 
        def showData(self):
                print("ID\t\t:",self.id)
                print("Name\t:",self.name)
                print("Designation\t:",self.desg)
                print("Salary\t:",self.sal)
                print("City\t:",self.city)




a=employee(101,'bhushan','dev',600000,'yavatmal')
a.showData()
'''	
if __name__=="__main__":
        main()	
'''

