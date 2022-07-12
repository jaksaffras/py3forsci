from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

for knight_name, knight_info in knight_data.items():
    # print(knight_name, knight_info)
    print(f"{knight_info[0]:4s} {knight_name:8s} {knight_info[1]}")

print("knight_data['Robin'][1]: {}".format(knight_data['Robin'][1]))
print("knight_data['Galahad'][2]: {}".format(knight_data['Galahad'][2]))
