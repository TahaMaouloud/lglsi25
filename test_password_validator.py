import pytest
from lglsi25.password_validator import validate_password
def test_validate_password():
    assert validate_password("Abcd1234!") == True
    assert validate_password("P@ssw0rd") == True
    assert validate_password("LongPassword123$") == True

    assert validate_password("abcd1234!") == False
    assert validate_password("ABCD1234!") == False
    assert validate_password("Abcdefgh!") == False
    assert validate_password("Abcd1234") == False
    assert validate_password("Ab1!") == False
    assert validate_password("") == False
    assert validate_password("        ") == False
    assert validate_password("12345678!") == False
    assert validate_password("abcdefgh!") == False
    assert validate_password("ABCDEFGH!") == False
