colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(colors), min(colors), max(colors), sorted(colors), '\n')
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums), '\n')

r = reversed(colors)
print("r: {}".format(r))
# print(r[0])  # chartreuse??
# print(len(r))
for color in r:
    print(color)
print()

print("Round 2:")
for color in r:
    print(color)
print()

print("Done.\n")

for color in colors:
    print(color)
print()

for i, color in enumerate(colors):
    print(i, color)
print()
print(list(enumerate(colors)))
print()

x = list(enumerate(colors))

for i in range(10):   #  range(stop)  range(start, stop)   range(start, stop, step)
    print(i, "Python is the best!!")
print()

for _ in range(5):
    print("Wombats")
print()

for i in range(1, 11):
    print(i, end=',')
print('\n')
