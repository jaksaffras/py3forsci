food_counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()

        if food in food_counts:
            food_counts[food] += 1   #  food_counts[food] = food_counts[food] + 1
        else:
            food_counts[food] = 1  # first time for this food

print("food_counts: {}".format(food_counts))
print()
for food, count in sorted(food_counts.items()):
    print(food, count)
