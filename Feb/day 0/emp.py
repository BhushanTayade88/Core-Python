class employee:
	empid=0
	empname=""
	empdesg=""
	empsal=0
	empcity=""

def setData(self):
	self.empid=int(input("Enter ID\t:"))
	self.empname=input("Enter Name\t:")
	self.empdesg=input("Enter Designation\t:")
	self.empsal=int(input("Enter salary\t:"))
	self.empcity=input("Enter City\t:")

def showData(self):
        print("ID\t\t:",self.empid)
        print("Name\t:",self.empname)
        print("Designation\t:",self.empdesg)
        print("Salary\t:",self.empsal)
        print("City\t:",self.empcity)

def main():
	a=employee()
	a.setData()
	a.showData()

if __name__=="__main__":
        main()	
