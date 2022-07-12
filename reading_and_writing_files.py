file_path = 'DATA/mary.txt'

mary_in = open(file_path, 'r')
mary_in.close()
print("type(mary_in): {}".format(type(mary_in)))

with open(file_path) as mary_in:
    # do something here...
    pass  # do-nothing statement
print()

# read one line at a time
with open(file_path) as mary_in:
    for raw_line in mary_in:
        # print("raw line:", repr(raw_line))
        line = raw_line.rstrip()
        # print("trimmed line:", repr(line))
        print(line)
print('-' * 60)

# read entire file into a single string
with open(file_path) as mary_in:
    contents = mary_in.read()
    print("raw contents:", repr(contents))
    print('=' * 20)
    print("normal contents:", contents)
print('-' * 60)

# read entire file into list of lines with newlines
with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# read entire file into list of lines without newlines
with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        term, last_name, first_name, dob, dod, birthplace, state, took_office, left_office, party = line.split(':')
        if party == 'Whig':
            print(line)
print('-' * 60)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit.capitalize() + '\n')
print()


with open('DATA/presidents.txt') as pres_in:
    with open('republicans.txt', 'w') as rep_out:
        with open('democrats.txt', 'w') as dem_out:
            with open('other.txt', 'w') as other_out:
                for raw_line in pres_in:
                    line = raw_line.rstrip()
                    term, last_name, first_name, dob, dod, birthplace, state, took_office, left_office, party = line.split(':')
                    data = f"{first_name} {last_name}\n"
                    if party == 'Democratic':
                        dem_out.write(data)
                    elif party == 'Republican':
                        rep_out.write(data)
                    else:
                        other_out.write(data)
