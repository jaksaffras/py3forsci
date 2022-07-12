import sys

a = "foo"
b = "bar"

x = [1, 2, 3]
y = [4, 5, 6]

f = a + b
m = x + y
print("f: {}".format(f))
print("m: {}".format(m))

print('-' * 60)
print("WOMBATS! " * 5)
flags = [True] * 10
print("flags: {}".format(flags))

print("sys.maxsize: {}\n".format(sys.maxsize))


colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

for color in 'pink', 'blue', 'scarlet', 'black', 'red', 'tan':
    print(color, color in colors)  # not in
print()


