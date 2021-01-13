list1 = list()  # new, empty list
list2 = [1, 2, 3]  # literal list
list3 = []  # new, empty list

cities = ['Pittsburgh', 'Sewickley', 'McKeesport',
          'Red Bank', 'Princeton', 'Newark']

print(len(cities))
print(cities[0], cities[3])
print(cities[-1])  # cities[len(cities)-1]

cities.append('Trenton')
cities.append('Moon Township')

print(cities)

more_cities = ['Elizabeth', 'Bergen', 'Parsippany']
cities.extend(more_cities)
print(cities)

# ITERABLE
# cities.extend('weird')
# print(cities)

cities.insert(0, 'Harrisburg')
cities.insert(5, 'Confluence')
print(cities)

# L.append(object) L.extend(iterable) L.insert(position, object)

cities[4] = 'Asbury Park'
print(cities)

del cities[2]  # del <any object>
print(cities)

x = 5
print(x)
del x
# print(x)

cities.remove('Newark')

print(cities)

c = cities.pop()
print("c is", c)
print(cities)

c = cities.pop(2)
print(c)
print(cities)

# del LIST[pos]   LIST.pop() LIST.pop(pos)  LIST.remove(value)
print(cities[0], cities[3], cities[-1])

print(cities[0:3])  # slice from 0 to 2

print(cities[4:7])  # elements 4, 5, 6

# LIST[START:STOP]   START is INclusive STOP is EXclusive
print(cities[4:8])

print(cities[:3])
print(cities[5:])
print(cities[-3:])

animal = "Pine Marten"
print(animal[:4], animal[5:9], animal[-3:])

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
print(food.count('spam'))
print(food.count('eggs'))
print(food.count('lobster thermidor'))
print()

for city in cities:
    print(city.upper())

print()

# for VAR in ITERABLE:
#    VAR = next element of ITERABLE
#    ....

# if elif else for while with class def try except finally