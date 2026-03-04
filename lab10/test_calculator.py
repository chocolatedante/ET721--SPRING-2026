"""
Dante Vanderpool
march 3 2026
lab 10, unit testing with pytest
"""
from calculator import *
import pytest


def test_add():
    assert add(2,3) == 5
    assert add(-8,5) == -3

def test_subtract():
    assert subtract(-7,-5) == -2

#lab exercise 1
def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(3,0)

#lab exercise 2
def test_valid_password():
    assert validate_password("peter$pan") is True

def test_short_password():
    assert validate_password("pan") is False

def test_special_character():
    assert validate_password("peter#pan") is False    

#lab exercise 3 
#parametrized test allows to run the same test with the different inputs
@pytest.mark.parametrize(
    "n, expected", 
    [
        (8, True),
        (-5, False), 
        (0, False),
        (-12, True),
        (11, False)
    ]
)    
def test_is_even(n, expected):
    assert is_even(n) == expected

#lab exercise 4
#create a parametied test for exercise 2
from calculator import validate_password

@pytest.mark.parametrize("password,expected", [
    ("peter$pan", True),   # valid
    ("pan", False),        # too short
    ("peter#pan", False),  # contains #
    ("peter%pan", False),  # contains %
    ("peter pan", False),  # contains space
])
def test_validate_password(password, expected):
    assert validate_password(password) is expected