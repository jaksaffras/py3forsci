from math import pi

def get_message():
    return "Hello, Python world"

m = get_message()
print(m)

def display_message():
    msg = get_message()
    print(msg)

display_message()

def circle_area(diameter):
    radius = diameter / 2
    area = pi * radius ** 2
    return area

a1 = circle_area(22)
a2 = circle_area(5)
a3 = circle_area(98.6)
print(a1, a2, a3)

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 10))
print(rectangle_area(2.3, 5.9))

def find_lines(search_term, *file_paths):
    print("file_paths: {}".format(file_paths))

    found = []
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    found.append(raw_line.rstrip())
    return found

lines = find_lines('bird', 'DATA/alice.txt', 'DATA/parrot.txt', 'DATA/words.txt')
for line in lines:
    print(line)
print()

lines = find_lines('wombat')
print(lines, '\n')


def hello(whom="WORLD"):
    print(f"Hello, {whom}")

hello("world")
hello("Mom")
hello("Dad")
hello()












