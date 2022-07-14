import sys
# from pkg.pkg import module
from john.mathlib import geometry

print("geometry.circle_area(1.5): {}".format(geometry.circle_area(1.5)))
print("geometry.rectangle_area(5, 9.6): {}".format(geometry.rectangle_area(5, 9.6)))
print()
for path in sys.path:  # curr folder + PYTHONPATH + builtin
    print(path)



