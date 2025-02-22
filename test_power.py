from power import power

def test_power():
    assert power(2, 3) == 8  # 2^3 = 8
    assert power(5, 0) == 1  # Any number to the power of 0 is 1
    assert power(3, 2) == 9  # 3^2 = 9
    assert power(2, -2) == 0.25  # 2^-2 = 1/4 = 0.25
