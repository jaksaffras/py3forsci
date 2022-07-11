i = 0
while i < 3:
    print(i)
    i += 1
print()

# user_name = None
# while user_name != 'q':
#     user_name = input("Enter name:")
#     print("User name:", user_name)

while True:
    user_name = input("Enter name:")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        print("...please enter a name")
        continue  # go back to top
    print("User name:", user_name)
