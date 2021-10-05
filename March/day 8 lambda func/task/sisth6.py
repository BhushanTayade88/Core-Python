'''
6.Write a Python program to find palindromes in a given list of strings using Lambda.
texts = ["php", "wow", "Python", "abcd", "Java", "aaa"]
List of palindromes:
['php', 'wow','aaa']
'''
exts = ["php", "wow", "Python", "abcd", "Java", "aaa"]
result=list(filter(lambda w:len(w)==3,exts))
print(result)

result2=list(filter(lambda x: (x == x[::-1]),exts))
print(result2)
a="bhushan"
c="nahsuhb"
b=a[::-1]
print(b)

##if "".join(reversed(a))==c:
##    print(c)
#print(list((reversed(a))))
result3=list(filter(lambda x: (x == "".join(reversed(x))),exts))
print(result3)
