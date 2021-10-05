'''
9.
state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 

Expected output:
{'Rajasthan':'Jaipur','Maharashtra': 'Mumbai','Gujarat':'Gandhinagar'}
'''
state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 


d={}
d=dict(zip(state,capital))
print(d)
d2={state[i]:capital[i] for i in range(len(state))}
print(d2)
