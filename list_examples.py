import sys


list1 = list()  # empty list

# x = list(any-iterable)

s = "abc"
list2 = list(s)
print("list2: {}".format(list2))

list3 = ['blue', 'purple', 'red']
list4 = []  # empty list

cities = ['Topeka', 'Portland', 'Denver', 'Bangalore']
print("len(cities): {}".format(len(cities)))

cities.insert(0, "Milan")
print("cities: {}".format(cities))
cities.insert(3, "Florence")
print("cities: {}".format(cities))
cities.append("Venice")
cities.append("Dubai")
print("cities: {}".format(cities))

more_cities = ['Bonn', 'Berlin', 'Frankfurt', 'Munich']
cities.extend(more_cities)
print("cities: {}".format(cities))

#  LIST.insert(pos, obj)   LIST.append(obj)  LIST.extend(iterable)

# more_junk = ['a', 'b', 'c']
# cities.append(more_junk)
# print("cities: {}".format(cities))

del cities[8]
print("cities: {}".format(cities))
pos = cities.index('Frankfurt')
print("pos: {}".format(pos))
del cities[pos]

cities.remove('Topeka')  #  del cities[cities.index('Topeka')]
print("cities: {}".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(2)
print("city: {}".format(city))
print("cities: {}".format(cities))

#  del LIST[pos]   LIST.remove(value)    x = LIST.pop(pos=-1)

print("cities[0]: {}".format(cities[0]))
print("cities[4]: {}".format(cities[4]))
print("cities[6]: {}".format(cities[6]))
print("cities[len(cities)-1]: {}".format(cities[len(cities)-1]))
print("cities[-1]: {}".format(cities[-1]))

actor = "Chris Hemsworth"
print("actor[0]: {}".format(actor[0]))
print("actor[6]: {}".format(actor[6]))
print("actor[-1]: {}".format(actor[-1]))

print("cities: {}".format(cities))

print("cities[0:4]: {}".format(cities[0:4]))

#  LIST[START:SENTINEL]
print("cities[2:5]: {}".format(cities[2:5]))

print("actor: {}".format(actor))
print("actor[:5]: {}".format(actor[:5]))
print("actor[-5:]: {}".format(actor[-5:]))
print("cities[-3:]: {}".format(cities[-3:]))

print("cities: {}".format(cities))
print()

for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)
print()

for letter in actor:
    print(letter.upper(), end='/')
print('\n')

for city in cities[:4]:
    print(city)
print()

for city in cities[1:]:
    print(city)
print()

for thing in sys.argv[1:]:
    print("thing: {}".format(thing))
print()


for wombat in cities:
    print(wombat.upper())
print()

for fruit in cities[-3:]:
    print(fruit)
print()

