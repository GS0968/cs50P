import pytest
from bank import value

def test_0():
    assert value("Hello")== 0
    assert value("hello")== 0

def test_20():
    assert value("Hey")== 20
    assert value("hey")== 20
    assert value("HOWDY")== 20
    assert value("howdy")== 20

def test_100():
    assert value("Good Morning")== 100
    assert value("good morning")== 100

