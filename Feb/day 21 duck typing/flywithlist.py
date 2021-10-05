class Bird:
    def fly(self):
        print("Bird fly with their wings")

class Airplane:
    def fly(self):
        print("Airplane fly fuel")

class Baloon:
    def fly(self):
        print("Baloon can fly in air with the help air")



l=[Bird(),Airplane(),Baloon()]
for i in l:
    i.fly()
    

