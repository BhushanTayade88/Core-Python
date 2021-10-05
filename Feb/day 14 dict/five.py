'''
5.Delete set of keys from Python Dictionary
Given:

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
keysToRemove = ["name", "salary"]

Expected output:
{'city': 'New york', 'age': 25}
'''
sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
#for k,v in sampleDict.items():
keysToRemove = ["name", "salary"]
for i in keysToRemove:
    sampleDict.pop(i)
                   

print(sampleDict)
    
