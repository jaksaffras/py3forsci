from pprint import pprint

def main():
    d = read_data()
    pretty_print(d)
    print()
    print_knight_info(d)
    print()
    print(get_attribute(d, 'Lancelot', 2))
    print(get_attribute(d, 'Galahad', 3))

def read_data():
    knight_data = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment
    return knight_data

def pretty_print(data):
    pprint(data)

def print_knight_info(data):
    for knight_name, knight_info in data.items():
        # print(knight_name, knight_info)
        print(f"{knight_info[0]:4s} {knight_name:8s} {knight_info[1]}")

def get_attribute(data, knight, field):
    return data[knight][field]


main()
