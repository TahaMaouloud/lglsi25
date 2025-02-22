import pytest
from Circles import calcaire , calccirconference
def test_calculer_aire():
    assert calcaire(10) == 314.1592653589793
    assert calcaire(5.6) == 98.5203456165759
    assert calcaire(0) == 0.00

def test_calculer_circonference():
    assert calccirconference(10) == 62.83185307179586
    assert calccirconference(5.6) == 35.18583772020568
    assert calccirconference(0) == 0.00