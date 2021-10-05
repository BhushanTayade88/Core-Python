def Generator(n):
##    i = 0
##    while i < n :
##        yield i
##        i += 1
##x=Generator(5)
##for i in x:
##    print(i)
    i = 5
    while i > n :
        yield i
        i = i - 1
x=Generator(1)
for i in x:
    print(i)
