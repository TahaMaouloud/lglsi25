import pytest
from simple_utils import is_even, is_odd, is_positive, square

# Tests for the 'is_even' function
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True  # 0 is considered even

# Tests for the 'is_odd' function
def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(0) == False  # 0 is not odd

# Tests for the 'is_positive' function
def test_is_positive():
    assert is_positive(5) == True
    assert is_positive(-5) == False
    assert is_positive(0) == False  # 0 is not positive

# Tests for the 'square' function
def test_square():
    assert square(3) == 9
    assert square(-3) == 9
    assert square(0) == 0