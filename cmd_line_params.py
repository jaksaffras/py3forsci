import sys

print("sys.argv: {}".format(sys.argv))

print("sys.argv[0]: {}".format(sys.argv[0]))
print("sys.argv[1]: {}".format(sys.argv[1]))
print(f"sys.argv[1]: {sys.argv[1]}")
print("sys.argv[1]:", sys.argv[1])


temp = float(sys.argv[1])

print(int(temp * 20))

