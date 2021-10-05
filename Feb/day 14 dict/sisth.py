'''
6.Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}

Expected output:
True
'''
sampleDict = {'a': 100, 'b': 200, 'c': 300}
for k,v in sampleDict.items():
    if v==200:
        print("true")

print(120 in sampleDict.values())
