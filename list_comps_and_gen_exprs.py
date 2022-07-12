fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

# [EXPR for VAR in ITERABLE]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [len(f) for f in fruits]
print("f2: {}\n".format(f2))

f3 = [(len(f), f.capitalize()) for f in fruits]
print("f3: {}\n".format(f3))

f4 = [f.upper() for f in fruits if f.startswith('p')]
print("f4: {}\n".format(f4))

f5 = [f for f in fruits if f.startswith('a')]
print("f5: {}\n".format(f5))

cities = ['Durham', 'Topeka', 'Albany', 'Buffalo', 'Portland', 'Topeka',
          'Pittsburgh', 'Los Angeles', 'Topeka']

c2 = [c for c in cities if c != 'Topeka']
print("c2: {}\n".format(c2))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print("dobs: {}\n".format(dobs))

dobs = [p[-1] for p in people if p[0] == 'Larry']
print("dobs: {}\n".format(dobs))


dobs_gen = (p[-1] for p in people)  # generator expression
print("dobs_gen: {}".format(dobs_gen))
for dob in dobs_gen:
    print(dob)
print()

pfruits_gen = (f.upper() for f in fruits if f.startswith('p'))
for fruit in pfruits_gen:
    print(fruit)
print()
