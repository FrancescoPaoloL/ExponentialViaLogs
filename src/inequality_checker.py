import math

def is_x_y_greater(x, y):
    if x <= 0 or y <= 0:
        return False  # Logarithm is undefined for non-positive numbers

    if x == y:
        return False  # x^x is not greater than x^x

    if x < math.e and y < math.e:
        return x**y > y**x

    return x < y

