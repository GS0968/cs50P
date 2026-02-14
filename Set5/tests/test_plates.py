import pytest
from plates import is_valid

def test_alphaonly():
    assert is_valid("COMP")==True
    assert is_valid("COMPSCI")==False

def test_alphanumericlen():
    assert is_valid("AAA222")==True
    assert is_valid("AAA22")==True
    assert is_valid("AA222")==True
    assert is_valid("AA22")==True
    assert is_valid("AA2")==True
    assert is_valid("A22")==False

def test_zeroplacement():
    assert is_valid("AA022")==False
    assert is_valid("AA220")==True

def test_numberplacement():
    assert is_valid("01AQD")==False
    assert is_valid("CS50P")==False
    assert is_valid("CS50")==True
    assert is_valid("CS05")==False
    assert is_valid("98765")== False
    assert is_valid("0987")== False

def test_length():
    assert is_valid("AAAAAAA")==False
    assert is_valid("AAAAAA")==True
    assert is_valid("AA")==True
    assert is_valid("A")==False

def test_alphanumeric():
    assert is_valid("AA!22")==False
    assert is_valid("AA22")==True

