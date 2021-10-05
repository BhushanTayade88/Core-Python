'''
4.Python program to create a list which contains the values having length of 6 using Lambda.
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Output:
Monday
Friday
Sunday
'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
result=list(filter(lambda w:len(w)==6,weekdays))
print(result)
