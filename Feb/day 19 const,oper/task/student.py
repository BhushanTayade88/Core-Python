class Student:
	def __init__(self,sturollno,stuname,marks):
		self.sturollno=sturollno
		self.stuname=stuname
		self.marks=marks
		
	def __str__(self):

                return f'Student RollNo: {self.sturollno}, Student name  :{self.stuname} and  Student Marks :{self.marks}'
            
		
