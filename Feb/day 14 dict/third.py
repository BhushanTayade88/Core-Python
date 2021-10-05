'''
3.Access the value of key ‘history’
sampleDict = { "class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
        
Expected output:

80
'''
sampleDict = { "Class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
for i in sampleDict:
    
    for Class in i:
        for student in Class:
            for marks in student:
                for c,v in marks.items():
                    print(c)
                
