from isprime import is_prime
def test_is_prime():
    test_cases = {
        2: True,
        3: True,
        4: False,
        5: True,
        9: False,
        13: True,
        15: False,
        19: True,
        25: False,
        29: True,
        1: False,
        0: False,
        -7: False,
    }

    for num, expected in test_cases.items():
        result = is_prime(num)
        assert result == expected, f"Test failed for {num}: Expected {expected}, got {result}"
    
    print("All tests passed!")


# Run tests
test_is_prime()