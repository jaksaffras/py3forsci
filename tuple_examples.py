
person = ('Bill', 'Gates', 'Microsoft', '1955-10-28')  # tuple

#  var = item1, item2, item3, ...

print(person[0], person[1])
print("type(person): {}".format(type(person)))

first_name, last_name, product, dob = person   # tuple unpacking
#  first_name = person[0]
#  last_name = person[1]
#  etc etc

#   var1, var2, var3, ... = some-iterable

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

print("type(people): {}".format(type(people)))
print("type(people[0]): {}".format(type(people[0])))
print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))
print()
for person in people:
    print(person)
print('-' * 60)

for person in people:
    # person = people[0]
    # person = people[1]
    # etc
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = person[0]
    # first_name, last_name, product, dob = person[1]
    # etc etc
    print(first_name, last_name)
print('-' * 60)

colors = ['red', 'purple', 'pink', 'mauve']
c1, c2, c3, c4 = colors
print(c1, c2, c3, c4)
print()
x, y, z = "bam"
print(x)
print(y)
print(z)
print()







