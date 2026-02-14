from numb3rs import validate
import pytest

def test_positive():
    assert validate("127.0.0.1")==True
    assert validate("140.247.235.144")==True
    assert validate("255.255.255.255")==True

def test_negative():
    assert validate("257.1.3.4")==False
    assert validate("cat")==False
    assert validate("10.10.10.10.10")==False
    assert validate("8.8.8")==False
    assert validate("64.128.256.512")==False
    assert validate("1.1.1.1111")==False
    assert validate("000.001.010.100")==False
