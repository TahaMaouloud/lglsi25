from sum_of_digits import sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(12) == 3
    assert sum_of_digits(6) == 6
    assert sum_of_digits(-9) == 9
    assert sum_of_digits(-666) == 18

test_sum_of_digits()