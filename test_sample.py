import pytest
import sample
def test_division():
    with pytest.raises(ValueError):
        sample.division(4,0)