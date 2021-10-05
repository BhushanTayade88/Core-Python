marks=[10,20,30,40,50,60,70,80,90,95]

failed_student = list(filter(lambda m:m<40,marks))
print(failed_student)


pass_student = list(filter(lambda m:m>=40,marks))
print(pass_student)
