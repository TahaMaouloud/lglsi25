# hypotenuse.py

import math

def calculate_hypotenuse(a, b):
    """
    Function to calculate the hypotenuse of a right-angled triangle
    using the Pythagorean theorem.

    Parameters:
    a (float): Length of one side of the triangle
    b (float): Length of the other side of the triangle

    Returns:
    float: Length of the hypotenuse
    """
    return math.sqrt(a**2 + b**2)
