
person = 'Bob', 'Smith', 'Milwaukee'




def display_name(person):
    first_name, last_name, city = person
    print(first_name, last_name)


display_name(person)

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        _, first_name, last_name, *_, party = line.split(':')
        print(first_name, last_name, party)
print('-' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
