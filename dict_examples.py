d1 = dict()  # empty dict
d2 = {'a':5, 'm':33, 'r': 99, 'e':15}
d3 = {}  # empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print("type(airports): {}".format(type(airports)))
print("len(airports): {}".format(len(airports)))

airports['PDX'] = 'Portland'
airports['FLR'] = 'Florence'

print("airports: {}".format(airports))

airports['FLR'] = 'Firenze'
print("airports: {}".format(airports))

print("airports['IAD']: {}".format(airports['IAD']))
print("airports['FLR']: {}".format(airports['FLR']))

for code in 'RDU', 'LAX', 'VIE', 'EWR', 'OAK', 'MIA':
    print(code, code in airports)
print()

airports['MIA'] = 'Miami'

# print("airports['MIA']: {}".format(airports['MIA']))
print("airports.get('MIA')): {}".format(airports.get('MIA')))
print("airports.get('MIA', 'missing')): {}".format(airports.get('MIA', 'missing')))
print("airports.get('MIA', 0)): {}".format(airports.get('MIA', 0)))


print("airports.items(): {}\n".format(airports.items()))

#  for key, value in DICT.items():
#      ...
for code, name in sorted(airports.items()):
    print(code, name)
print()

for x in airports:  # airports.keys()
    print(x)
print()

if 'LAX' in airports:
    print(airports['LAX'])
else:
    print("awwwwww")

print(airports.get('LAX', 'awwww'))
