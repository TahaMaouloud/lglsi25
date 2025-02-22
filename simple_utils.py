def is_even(n: int) -> bool:
    """Returns True if the number is even, False otherwise."""
    return n % 2 == 0

def is_odd(n: int) -> bool:
    """Returns True if the number is odd, False otherwise."""
    return n % 2 != 0

def is_positive(n: int) -> bool:
    """Returns True if the number is positive, False otherwise."""
    return n > 0

def square(n: int) -> int:
    """Returns the square of the number."""
    return n * n