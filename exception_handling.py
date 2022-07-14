file_path = "DATA/wombats.txt"

class JohnError(Exception):
    pass

try:
    raise JohnError("This is easy!")
except JohnError as err:
    print(err)

try:
    with open(file_path) as wombats_in:
        for raw_line in wombats_in:
            line = raw_line.rstrip()
            print(line)
except (FileNotFoundError, PermissionError) as err:
    print(err)
except JohnError as err:
    print("Wow!", err)
except Exception as err:
    print(err)

file_path = "DATA/breakfast.txt"
with open(file_path) as breakfast_in:
    food = breakfast_in.read().splitlines()

print("len(food): {}".format(len(food)))

try:
    value = food[98]
    print("value: {}".format(value))

except IndexError as err:
    print(err)


nums = [0, 800, 80, 1000, 32, 255, 400, 0, 5, 5000]
for n in nums:
    try:
        result = 28 / n
    except ZeroDivisionError as err:
        print(err)
    else:
        print(n, result)

print("All done!")


