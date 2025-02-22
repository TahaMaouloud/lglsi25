import pytest
from combination import comb
def test_combination_allowed():
    assert comb(0,0)==1
    assert comb(1,1)==1
    assert comb(3,2)==3

def test_combination_notallowed():
    with pytest.raises(ValueError):
        comb(3,-3)
    with pytest.raises(ValueError):
        comb(1,3)
    with pytest.raises(TypeError):
        comb(1.5,0.8)
    with pytest.raises(TypeError):
        comb(8,"a")