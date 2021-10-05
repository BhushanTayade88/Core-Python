import ast
from emp import *

print("----Statements----\n" \
      "1.Enter details--\n" \
      "2.display--\n" \
      "3.Exit--\n")

	
list2=[]

while True:
	e=ast.literal_eval(input("Enter elements :"))
	list2.append(e)
	choice = input("want to stop ? then press 'y' otherwise press any key :")
	if choice == "y":
		break
print("Show elements in list  :")

for emp in list2:
	print(emp)

	

