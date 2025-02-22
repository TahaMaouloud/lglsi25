import pytest
from perfect import is_perfect
def test_perfect_number():

    assert is_perfect(6) == True   
    assert is_perfect(28) == True   
    assert is_perfect(496) == True  

def test_non_perfect_number():
    assert is_perfect(1) == False 
    assert is_perfect(10) == False  
    assert is_perfect(12) == False  
    assert is_perfect(100) == False 

def test_edge_cases():
    assert is_perfect(0) == False
    assert is_perfect(-6) == False  
