
value_a = 56

if value_a > 75:
    print("Kangaroo")
    print("Koala")
elif value_a > 50:  # else if
    print("Wallaby")
    print("Wombat")
else:
    print("Quokka")
    print("Tasmanian devil")

print("Done")


# X is Boolean False if
# X is False
# X = 0 numerically
# len(X) == 0  # "container" with zero elements
# X is None

#  True (== 1)
#  False (== 0)

DEBUG = True

color = "red" if DEBUG else "blue"
print("color: {}".format(color))


if DEBUG:
    color = "red"
else:
    color = "blue"



count = 0 if len(color) < 5 else 100
print("count: {}".format(count))

# color = ''

def spam(x):
    print("x: {}".format(x))



spam(100 if color else 25)

#  == != > < >= <=

#  and or not

if (color != 'blue') and (len(color) < 10):
    print("sphagnum moss")








