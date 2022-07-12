
with open('DATA/breakfast.txt') as breakfast_in:
    all_foods = breakfast_in.read().splitlines()
    # print(all_foods)
    unique_foods = set(all_foods)
    print("unique_foods: {}".format(unique_foods))

fruits1 = ['banana', 'kiwi', 'orange', 'lime', 'durian', 'apple', 'peach', 'pomegranate', 'pineapple']
fruits2 = ['pineapple', 'persimmon', 'lychee', 'peach', 'apple', 'apricot', 'orange', 'orange', 'orange', 'blueberry',
           'pear', 'banana']

f1 = set(fruits1)
f2 = set(fruits2)
f2.add('lemon')
f1.add('watermelon')
print("f1: {}".format(f1))
print("f2: {}".format(f2))

print("common:", f1 & f2)  # intersection
print("NOT common:", f1 ^ f2) # xor
print("all:", f1 | f2)  #  union
print("lychee" in f1)
print("lychee" in f2)
print("only f1:", f1 - f2)
print("only f2:", f2 - f1)





