
LIMIT = 20

flags = [True] * (LIMIT + 1)
# print("flags: {}".format(flags))

for num in range(2, LIMIT + 1):
    print("num:", num)

    if flags[num]:  # is it prime??
        print("prime:", num)
        for multiple in range(num * 2, LIMIT + 1, num):
            flags[multiple] = False
    # else
    #    NOT PRIME
    print("flags:", flags)

