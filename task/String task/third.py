'''
3.Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

Output:
mixString("America", "Japan") = "AJrpan"
string taken fmuser
'''
a="America"
b="Japan"

first =(a[0]+b[0])
#middle=(a[3]+b[2])
last=(a[-1]+b[-1])
sec=a[3:4]
second = a[int(len(a) / 2):int(len(a) / 2) + 1] + b[int(len(b) / 2):int(len(b) / 2) + 1]
middle = a[int(len(a)/2)]+b[int(len(b)/2)]
print(middle)
print(first+middle+last)
conc = ''
for i in range(len(a)):
    for j in range(len(b)):
        # if i==0 or i==int(len(a)/2) or i==len(a)-1:
            if i==0:
                conc = conc+a[i]+b[j]
                break
            elif i==int(len(a)/2) and j==int(len(b)/2):
                conc += a[i]+b[j]
                break
            elif i==len(a)-1:
                conc += a[i]+b[-1]
                break
print(conc,"using loop")
         


