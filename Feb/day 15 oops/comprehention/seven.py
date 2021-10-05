'''
Given a list,
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
Find the planets whose length is less than 6.

'''
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
l2=[]
for i in planets: 
    for planet in i: 
          
        if len(planet) < 6: 
            l2.append(planet)
            
          
print(l2) 
l3=[j for i in planets for j in i if len(j)<6]
print(l3)
