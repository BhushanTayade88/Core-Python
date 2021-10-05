'''
Que 1)Given the following dictionary:

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
Try to do the followings:

1.Add a key to inventory called 'pocket'.
2.Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
3.sort()the items in the list stored under the 'backpack' key.
4.remove('dagger') from the list of items stored under the 'backpack' key.
5.Add 50 to the number stored under the 'gold' key.

output at last:
{'pocket': ['seashell', 'strange berry', 'lint'], 'backpack': ['bedroll', 'bread loaf', 'xylophone'], 'pouch': ['flint', 'twine', 'gemstone'], 'gold': 550}

'''
inventory = {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],
             'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

inventory["pocket"] =  ["seashell", "strange berry", "lint"]
print(inventory)
inventory['backpack'].sort()
print(inventory)
inventory['backpack'].remove("dagger")
print(inventory)
inventory['gold']=50
print(inventory)
