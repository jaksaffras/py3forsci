

# local, nonlocal, global, builtin

x = 100

def spam():
    x = 25
    color = "blue"  # local scope
    print("in spam -- x: {}".format(x))


def foo():
    x = 10

    def bar():
        print("x is", x)




print("x: {}".format(x))
spam()

# print("color: {}".format(color))


