'''
4.Given a list,
l = ['Red','Green','Blue']

Expected output:
{'blue':'BLUE','green':'GREEN','red':'RED'}
'''
l = ['Red','Green','Blue']
d={i.lower():i.upper() for i in l}
print(d)
