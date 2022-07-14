"""
Misc math routines
"""
from math import pi

def circle_area(diameter):
    """
    Calculate area of circle.

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    area = pi * radius ** 2
    return area

def rectangle_area(length, width):
    """
    Calculate area of rectangle

    :param length: Length of rectangle
    :param width: Width of rectangle
    :return: Area of rectangle
    """
    return length * width

if __name__ == '__main__':  # if executed directly, not imported
    a = circle_area(1)
    b = rectangle_area(1, 2)
    print("TESTING:", a, b)
