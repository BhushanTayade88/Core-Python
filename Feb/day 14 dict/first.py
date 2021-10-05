
'''
1.Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
by zip and dict comprehention
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d={}
for i in range(len(keys)):
               d[keys[i]]=values[i]
               print(d)
        
   
              
print(d)                    
        
        
        

