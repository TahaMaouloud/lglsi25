import pytest
from amicable_numbers import are_amicable

def test_amicable_numbers():
    assert are_amicable(220, 284) == True  # 220 et 284 sont amis
    assert are_amicable(1184, 1210) == True  # 1184 et 1210 sont amis
    assert are_amicable(2620, 2924) == True  # 2620 et 2924 sont amis
    assert are_amicable(10, 20) == False  # 10 et 20 ne sont pas amis
    assert are_amicable(6, 6) == False  # 6 et 6 ne sont pas amis
    assert are_amicable(220, 221) == False  # 220 et 221 ne sont pas amis

if __name__ == "__main__":
    pytest.main()
