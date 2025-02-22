# test_hypotenuse.py

import pytest
from hypotenuse import calculate_hypotenuse

def test_positive_values():
    assert calculate_hypotenuse(3, 4) == 5  # Common 3-4-5 triangle
    assert calculate_hypotenuse(5, 12) == 13  # Common 5-12-13 triangle
    assert calculate_hypotenuse(8, 15) == 17  # Common 8-15-17 triangle

def test_zero_values():
    assert calculate_hypotenuse(0, 0) == 0  # If both sides are 0, hypotenuse should be 0
    assert calculate_hypotenuse(0, 3) == 3  # If one side is 0, hypotenuse should be the other side
    assert calculate_hypotenuse(5, 0) == 5  # If one side is 0, hypotenuse should be the other side

def test_negative_values():
    # Hypotenuse can't be calculated with negative side lengths, handle invalid input gracefully
    with pytest.raises(ValueError):
        calculate_hypotenuse(-3, 4)
    
    with pytest.raises(ValueError):
        calculate_hypotenuse(3, -4)
    
    with pytest.raises(ValueError):
        calculate_hypotenuse(-3, -4)

def test_float_values():
    assert calculate_hypotenuse(3.5, 4.5) == pytest.approx(5.7, rel=1e-2)  # Approximate value check for floating point sides

