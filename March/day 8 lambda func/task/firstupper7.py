

'''
7.Given a list,
l = ['cat','dog','dow','sheep']
Make the first character of words into capital.
'''
l = ['cat','dog','dow','sheep','cjc']
l2=list(map(lambda a:a.title() ,l))
print(l2)


result3 = list(filter(lambda x: (x == "".join(reversed(x))), l))
print(result3)
