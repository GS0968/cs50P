import pytest
from fuel import gauge
from fuel import convert

def test_converterror():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_convertintcheck():
    assert convert("4/4")==100
    assert convert("3/4")==75
    assert convert("0/4")==0

def test_gauge():
    assert gauge(0)=="E"
    assert gauge(1)=="E"
    assert gauge(50)=="50%"
    assert gauge(99)=="F"
    assert gauge(100)=="F"
