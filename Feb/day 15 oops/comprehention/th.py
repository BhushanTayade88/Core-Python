'''
3.Delete set of keys from Python Dictionary
Given:

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
keysToRemove = ["name", "salary"]

Expected output:
{'city': 'New york', 'age': 25}
'''
sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
keysToRemove = ["name", "salary"]
#sampleDict={k:sampleDict[k] for k in sampleDict.keys()-keysToRemove}
sampleDict={k:sampleDict[k] for k in sampleDict.keys() if k not in keysToRemove}
print(sampleDict)
