'''
8.ages = [13, 90, 17, 59, 21, 60, 5] Make a new list as 'adults' which contains age greater than 18.
'''
ages = [13, 90, 17, 59, 21, 60, 5]
adults=list(filter(lambda a:a>18 ,ages))
print(adults)
