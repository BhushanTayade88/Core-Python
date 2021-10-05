'''
4.Create a new dictionary by extracting the following keys from a given dictionary
Given dictionary:

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}

Keys to extract
keys = ["name", "salary"]

Expected output:
{'name': 'Kelly', 'salary': 8000}
'''

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
keys = ["name", "salary"]
d2={}
for k in keys:
    d2[k]=sampleDict[k]
print(d2)
    
