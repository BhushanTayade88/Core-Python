import random
def phoneno():
    first = str(random.randint(777, 999))
    second = str(random.randint(0, 999))
    last = str(random.randint(0, 9998))
    return '{}{}{}'.format(first, second, last)
n = int(input("Enter Value of n: "))
for i in range(0, n):
    print(phoneno())


def phn():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]
print(phn())
