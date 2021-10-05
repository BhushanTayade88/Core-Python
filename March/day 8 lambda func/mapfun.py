marks=[10,20,30,40,50,60,70,80,90,95]
'''
def min(m):
    if m<40:
        return m
print(min(30))
'''


new_student = list(map(lambda m:m+5,marks))
print(new_student)

new_student = list(map(lambda m:m/2,marks))
print(new_student)
