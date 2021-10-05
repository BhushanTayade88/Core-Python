In [7]: def swap(d):
   ...:     new = {}
   ...:     for key, value in d.items():
   ...:         if value in new.keys():
   ...:             new[value].append(key)
   ...:         else:
   ...:             new[value] = [key]
   ...:     return new
   ...: 
