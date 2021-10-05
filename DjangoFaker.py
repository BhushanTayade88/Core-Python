from faker import Faker 
import random  

def phoneno():
    first = str(random.randint(777, 999))
    second = str(random.randint(0, 999))
    last = str(random.randint(0, 9998))
    return '{}{}{}'.format(first, second, last)  
fake = Faker()
for i in range(0, 10): 
    print('Name->', fake.name())
    print('Address-->', fake.address())
    print('Country->', fake.country())
##    fake.country_calling_code()==+91:    
    print('Phone-No-->', '+91',phoneno())
    print("-------------------------------------")



##import random as r 
##ph_no = []
##ph_no.append(r.randint(7, 9))
##  
##for i in range(1, 10):
##    ph_no.append(r.randint(0, 9))
##print(ph_no)
