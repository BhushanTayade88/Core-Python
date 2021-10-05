class car():
	def __init__(self,model,color):
		self.model=model
		self.color=color
	
	def show(self):
		print("Model is",self.model)
		print("Color is",self.color)

audi=car("Audi a4","black")
ferrari=car("Ferrari 488","white")


audi.show()
ferrari.show()